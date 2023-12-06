#####CONCURRENCY & THREADING



##THREADING WITHOUT TIME METHOD

# from time import sleep
#
# class A:
#     def run(self):
#         for i in range(5):
#             print("Aman bhaiya")
#             sleep(1)
#
# class B:
#     def run(self):
#         for i in range(5):
#             print("ajay bhaiya")
#             sleep(1)
#
# class C:
#     def run(self):
#         for i in range(5):
#             print("jalaj bhaiya")
#             sleep(1)
# t1=A()
# t2=B()
# t3=C()
#
# t1.run()
# t2.run()
# t3.run()

##THREADING WITH TIME:

# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("aman bhaiya")
#             sleep(1)
#
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("ajay bhaiya")
#             sleep(1)
#
# t1=A()
# t2=B()
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("jalaj")

