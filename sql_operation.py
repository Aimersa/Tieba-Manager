# -*- coding:utf-8 -*-
import argparse
import asyncio

import tiebaBrowser as tb
import tiebaBrowser.cloud_review as cr

if __name__ == '__main__':

    async def main():

        parser = argparse.ArgumentParser(
            description='MySQL操作', allow_abbrev=False)
        parser.add_argument('tieba_name',
                            type=str,
                            help='贴吧名')
        parser.add_argument('--id', '-i',
                            type=str,
                            help='用户id')
        parser.add_argument('--image', '-img',
                            type=str,
                            help='图像id')
        parser.add_argument('--post_id', '-p',
                            type=int,
                            help='白名单pid')

        parser.add_argument('--search', '-s',
                            action='store_true',
                            help='是否查询状态')
        parser.add_argument('--flag', '-f',
                            action='store_true',
                            help='是否设置为true')
        parser.add_argument('--delete', '-d',
                            action='store_true',
                            help='是否从表中删除')

        parser.add_argument('--delete_new', '-dn',
                            type=int,
                            help='是否删除最近n小时的pid记录',
                            metavar='HOUR')
        args = parser.parse_args()

        async with cr.CloudReview('default', args.tieba_name) as brow:

            if args.delete_new:
                await brow.mysql.del_pids(args.tieba_name, args.delete_new)

            if args.id:
                if args.delete:
                    await brow.del_user_id(args.id)
                elif args.search:
                    user = await brow.get_userinfo_weak(args.id)
                    print(await brow.mysql.is_user_id_white(args.tieba_name, user.user_id))
                else:
                    await brow.update_user_id(args.id, args.flag)

            if args.image:
                img_url = f"http://tiebapic.baidu.com/forum/pic/item/{args.image}.jpg"
                img = await brow.url2image(img_url)
                img_hash = brow.get_imghash(img)
                if img_hash:
                    if args.delete:
                        await brow.mysql.del_imghash(args.tieba_name, img_hash)
                    elif args.search:
                        print(await brow.mysql.has_imghash(args.tieba_name, img_hash))
                    else:
                        await brow.mysql.add_imghash(args.tieba_name, img_hash, args.image)

            if args.post_id:
                if args.delete:
                    await brow.mysql.del_pid(args.tieba_name, args.post_id)
                elif args.search:
                    print(await brow.mysql.has_pid(args.tieba_name, args.post_id))
                else:
                    await brow.mysql.add_pid(args.tieba_name, args.post_id)

    asyncio.run(main())