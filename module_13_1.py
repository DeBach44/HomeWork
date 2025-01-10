import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for number_ball in range(1, 6):
        await asyncio.sleep(5 - power)
        print(f'Силач {name} поднял {number_ball}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman(name='Николай', power=2))
    task_2 = asyncio.create_task(start_strongman(name='Сергей', power=3))
    task_3 = asyncio.create_task(start_strongman(name='Иван', power=4))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
