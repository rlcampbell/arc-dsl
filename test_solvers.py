import json

from solvers import *


with open("arc-agi_training_challenges.json") as fp:
    train_challenges = json.load(fp)


def runSolver(key):
    try:
        task = train_challenges[key]
    except:
        return
    train_inputs = [example["input"] for example in task["train"]]
    train_outputs = [example["output"] for example in task["train"]]
    solverFunction = globals()["solve_" + key]
    for i in range(len(train_inputs)):
        trainOut = tuple(tuple(inner_list) for inner_list in train_outputs[i])
        assert solverFunction(train_inputs[i]) == trainOut


def test_007bbfb7():
    runSolver("007bbfb7")


def test_00d62c1b():
    runSolver("00d62c1b")


def test_017c7c7b():
    runSolver("017c7c7b")


def test_025d127b():
    runSolver("025d127b")


def test_045e512c():
    runSolver("045e512c")


def test_0520fde7():
    runSolver("0520fde7")


def test_05269061():
    runSolver("05269061")


def test_05f2a901():
    runSolver("05f2a901")


def test_06df4c85():
    runSolver("06df4c85")


def test_08ed6ac7():
    runSolver("08ed6ac7")


def test_09629e4f():
    runSolver("xxxxx")


def test_0962bcdd():
    runSolver("xxxxx")


def test_0a938d79():
    runSolver("xxxxx")


def test_0b148d64():
    runSolver("xxxxx")


def test_0ca9ddb6():
    runSolver("xxxxx")


def test_0d3d703e():
    runSolver("xxxxx")


def test_0dfd9992():
    runSolver("xxxxx")


def test_0e206a2e():
    runSolver("xxxxx")


def test_10fcaaa3():
    runSolver("xxxxx")


def test_11852cab():
    runSolver("xxxxx")


def test_1190e5a7():
    runSolver("xxxxx")


def test_137eaa0f():
    runSolver("xxxxx")


def test_150deff5():
    runSolver("xxxxx")


def test_178fcbfb():
    runSolver("xxxxx")


def test_1a07d186():
    runSolver("xxxxx")


def test_1b2d62fb():
    runSolver("xxxxx")


def test_1b60fb0c():
    runSolver("xxxxx")


def test_1bfc4729():
    runSolver("xxxxx")


def test_1c786137():
    runSolver("xxxxx")


def test_1caeab9d():
    runSolver("xxxxx")


def test_1cf80156():
    runSolver("xxxxx")


def test_1e0a9b12():
    runSolver("xxxxx")


def test_1e32b0e9():
    runSolver("xxxxx")


def test_1f0c79e5():
    runSolver("xxxxx")


def test_1f642eb9():
    runSolver("xxxxx")


def test_1f85a75f():
    runSolver("xxxxx")


def test_1f876c06():
    runSolver("xxxxx")


def test_1fad071e():
    runSolver("xxxxx")


def test_2013d3e2():
    runSolver("xxxxx")


def test_2204b7a8():
    runSolver("xxxxx")


def test_22168020():
    runSolver("xxxxx")


def test_22233c11():
    runSolver("xxxxx")


def test_2281f1f4():
    runSolver("xxxxx")


def test_228f6490():
    runSolver("xxxxx")


def test_22eb0ac0():
    runSolver("xxxxx")


def test_234bbc79():
    runSolver("xxxxx")


def test_23581191():
    runSolver("xxxxx")


def test_239be575():
    runSolver("xxxxx")


def test_23b5c85d():
    runSolver("xxxxx")


def test_253bf280():
    runSolver("xxxxx")


def test_25d487eb():
    runSolver("xxxxx")


def test_25d8a9c8():
    runSolver("xxxxx")


def test_25ff71a9():
    runSolver("xxxxx")


def test_264363fd():
    runSolver("xxxxx")


def test_272f95fa():
    runSolver("xxxxx")


def test_27a28665():
    runSolver("xxxxx")


def test_28bf18c6():
    runSolver("xxxxx")


def test_28e73c20():
    runSolver("xxxxx")


def test_29623171():
    runSolver("xxxxx")


def test_29c11459():
    runSolver("xxxxx")


def test_29ec7d0e():
    runSolver("xxxxx")


def test_2bcee788():
    runSolver("xxxxx")


def test_2bee17df():
    runSolver("xxxxx")


def test_2c608aff():
    runSolver("xxxxx")


def test_2dc579da():
    runSolver("xxxxx")


def test_2dd70a9a():
    runSolver("xxxxx")


def test_2dee498d():
    runSolver("xxxxx")


def test_31aa019c():
    runSolver("xxxxx")


def test_321b1fc6():
    runSolver("xxxxx")


def test_32597951():
    runSolver("xxxxx")


def test_3345333e():
    runSolver("xxxxx")


def test_3428a4f5():
    runSolver("xxxxx")


def test_3618c87e():
    runSolver("xxxxx")


def test_3631a71a():
    runSolver("xxxxx")


def test_363442ee():
    runSolver("xxxxx")


def test_36d67576():
    runSolver("xxxxx")


def test_36fdfd69():
    runSolver("xxxxx")


def test_3906de3d():
    runSolver("xxxxx")


def test_39a8645d():
    runSolver("xxxxx")


def test_39e1d7f9():
    runSolver("xxxxx")


def test_3aa6fb7a():
    runSolver("xxxxx")


def test_3ac3eb23():
    runSolver("xxxxx")


def test_3af2c5a8():
    runSolver("xxxxx")


def test_3bd67248():
    runSolver("xxxxx")


def test_3bdb4ada():
    runSolver("xxxxx")


def test_3befdf3e():
    runSolver("xxxxx")


def test_3c9b0459():
    runSolver("xxxxx")


def test_3de23699():
    runSolver("xxxxx")


def test_3e980e27():
    runSolver("xxxxx")


def test_3eda0437():
    runSolver("xxxxx")


def test_3f7978a0():
    runSolver("xxxxx")


def test_40853293():
    runSolver("xxxxx")


def test_4093f84a():
    runSolver("xxxxx")


def test_41e4d17e():
    runSolver("xxxxx")


def test_4258a5f9():
    runSolver("xxxxx")


def test_4290ef0e():
    runSolver("xxxxx")


def test_42a50994():
    runSolver("xxxxx")


def test_4347f46a():
    runSolver("xxxxx")


def test_444801d8():
    runSolver("xxxxx")


def test_445eab21():
    runSolver("xxxxx")


def test_447fd412():
    runSolver("xxxxx")


def test_44d8ac46():
    runSolver("xxxxx")


def test_44f52bb0():
    runSolver("xxxxx")


def test_4522001f():
    runSolver("xxxxx")


def test_4612dd53():
    runSolver("xxxxx")


def test_46442a0e():
    runSolver("xxxxx")


def test_469497ad():
    runSolver("xxxxx")


def test_46f33fce():
    runSolver("xxxxx")


def test_47c1f68c():
    runSolver("xxxxx")


def test_484b58aa():
    runSolver("xxxxx")


def test_48d8fb45():
    runSolver("xxxxx")


def test_4938f0c2():
    runSolver("xxxxx")


def test_496994bd():
    runSolver("xxxxx")


def test_49d1d64f():
    runSolver("xxxxx")


def test_4be741c5():
    runSolver("xxxxx")


def test_4c4377d9():
    runSolver("xxxxx")


def test_4c5c2cf0():
    runSolver("xxxxx")


def test_50846271():
    runSolver("xxxxx")


def test_508bd3b6():
    runSolver("xxxxx")


def test_50cb2852():
    runSolver("xxxxx")


def test_5117e062():
    runSolver("xxxxx")


def test_5168d44c():
    runSolver("xxxxx")


def test_539a4f51():
    runSolver("xxxxx")


def test_53b68214():
    runSolver("xxxxx")


def test_543a7ed5():
    runSolver("xxxxx")


def test_54d82841():
    runSolver("xxxxx")


def test_54d9e175():
    runSolver("xxxxx")


def test_5521c0d9():
    runSolver("xxxxx")


def test_5582e5ca():
    runSolver("xxxxx")


def test_5614dbcf():
    runSolver("xxxxx")


def test_56dc2b01():
    runSolver("xxxxx")


def test_56ff96f3():
    runSolver("xxxxx")


def test_57aa92db():
    runSolver("xxxxx")


def test_5ad4f10b():
    runSolver("xxxxx")


def test_5bd6f4ac():
    runSolver("xxxxx")


def test_5c0a986e():
    runSolver("xxxxx")


def test_5c2c9af4():
    runSolver("xxxxx")


def test_5daaa586():
    runSolver("xxxxx")


def test_60b61512():
    runSolver("xxxxx")


def test_6150a2bd():
    runSolver("xxxxx")


def test_623ea044():
    runSolver("xxxxx")


def test_62c24649():
    runSolver("xxxxx")


def test_63613498():
    runSolver("xxxxx")


def test_6430c8c4():
    runSolver("xxxxx")


def test_6455b5f5():
    runSolver("xxxxx")


def test_662c240a():
    runSolver("xxxxx")


def test_67385a82():
    runSolver("xxxxx")


def test_673ef223():
    runSolver("xxxxx")


def test_6773b310():
    runSolver("xxxxx")


def test_67a3c6ac():
    runSolver("xxxxx")


def test_67a423a3():
    runSolver("xxxxx")


def test_67e8384a():
    runSolver("xxxxx")


def test_681b3aeb():
    runSolver("xxxxx")


def test_6855a6e4():
    runSolver("xxxxx")


def test_68b16354():
    runSolver("xxxxx")


def test_694f12f3():
    runSolver("xxxxx")


def test_6a1e5592():
    runSolver("xxxxx")


def test_6aa20dc0():
    runSolver("xxxxx")


def test_6b9890af():
    runSolver("xxxxx")


def test_6c434453():
    runSolver("xxxxx")


def test_6cdd2623():
    runSolver("xxxxx")


def test_6cf79266():
    runSolver("xxxxx")


def test_6d0160f0():
    runSolver("xxxxx")


def test_6d0aefbc():
    runSolver("xxxxx")


def test_6d58a25d():
    runSolver("xxxxx")


def test_6d75e8bb():
    runSolver("xxxxx")


def test_6e02f1e3():
    runSolver("xxxxx")


def test_6e19193c():
    runSolver("xxxxx")


def test_6e82a1ae():
    runSolver("xxxxx")


def test_6ecd11f4():
    runSolver("xxxxx")


def test_6f8cd79b():
    runSolver("xxxxx")


def test_6fa7a44f():
    runSolver("xxxxx")


def test_72322fa7():
    runSolver("xxxxx")


def test_72ca375d():
    runSolver("xxxxx")


def test_73251a56():
    runSolver("xxxxx")


def test_7447852a():
    runSolver("xxxxx")


def test_7468f01a():
    runSolver("xxxxx")


def test_746b3537():
    runSolver("xxxxx")


def test_74dd1130():
    runSolver("xxxxx")


def test_75b8110e():
    runSolver("xxxxx")


def test_760b3cac():
    runSolver("xxxxx")


def test_776ffc46():
    runSolver("xxxxx")


def test_77fdfe62():
    runSolver("xxxxx")


def test_780d0b14():
    runSolver("xxxxx")


def test_7837ac64():
    runSolver("xxxxx")


def test_794b24be():
    runSolver("xxxxx")


def test_7b6016b9():
    runSolver("xxxxx")


def test_7b7f7511():
    runSolver("xxxxx")


def test_7c008303():
    runSolver("xxxxx")


def test_7ddcd7ec():
    runSolver("xxxxx")


def test_7df24a62():
    runSolver("xxxxx")


def test_7e0986d6():
    runSolver("xxxxx")


def test_7f4411dc():
    runSolver("xxxxx")


def test_7fe24cdd():
    runSolver("xxxxx")


def test_80af3007():
    runSolver("xxxxx")


def test_810b9b61():
    runSolver("xxxxx")


def test_82819916():
    runSolver("xxxxx")


def test_83302e8f():
    runSolver("xxxxx")


def test_834ec97d():
    runSolver("xxxxx")


def test_8403a5d5():
    runSolver("xxxxx")


def test_846bdb03():
    runSolver("xxxxx")


def test_855e0971():
    runSolver("xxxxx")


def test_85c4e7cd():
    runSolver("xxxxx")


def test_868de0fa():
    runSolver("xxxxx")


def test_8731374e():
    runSolver("xxxxx")


def test_88a10436():
    runSolver("xxxxx")


def test_88a62173():
    runSolver("xxxxx")


def test_890034e9():
    runSolver("xxxxx")


def test_8a004b2b():
    runSolver("xxxxx")


def test_8be77c9e():
    runSolver("xxxxx")


def test_8d5021e8():
    runSolver("xxxxx")


def test_8d510a79():
    runSolver("xxxxx")


def test_8e1813be():
    runSolver("xxxxx")


def test_8e5a5113():
    runSolver("xxxxx")


def test_8eb1be9a():
    runSolver("xxxxx")


def test_8efcae92():
    runSolver("xxxxx")


def test_8f2ea7aa():
    runSolver("xxxxx")


def test_90c28cc7():
    runSolver("xxxxx")


def test_90f3ed37():
    runSolver("xxxxx")


def test_913fb3ed():
    runSolver("xxxxx")


def test_91413438():
    runSolver("xxxxx")


def test_91714a58():
    runSolver("xxxxx")


def test_9172f3a0():
    runSolver("xxxxx")


def test_928ad970():
    runSolver("xxxxx")


def test_93b581b8():
    runSolver("xxxxx")


def test_941d9a10():
    runSolver("xxxxx")


def test_94f9d214():
    runSolver("xxxxx")


def test_952a094c():
    runSolver("xxxxx")


def test_9565186b():
    runSolver("xxxxx")


def test_95990924():
    runSolver("xxxxx")


def test_963e52fc():
    runSolver("xxxxx")


def test_97999447():
    runSolver("xxxxx")


def test_97a05b5b():
    runSolver("xxxxx")


def test_98cf29f8():
    runSolver("xxxxx")


def test_995c5fa3():
    runSolver("xxxxx")


def test_99b1bc43():
    runSolver("xxxxx")


def test_99fa7670():
    runSolver("xxxxx")


def test_9aec4887():
    runSolver("xxxxx")


def test_9af7a82c():
    runSolver("xxxxx")


def test_9d9215db():
    runSolver("xxxxx")


def test_9dfd6313():
    runSolver("xxxxx")


def test_9ecd008a():
    runSolver("xxxxx")


def test_9edfc990():
    runSolver("xxxxx")


def test_9f236235():
    runSolver("xxxxx")


def test_a1570a43():
    runSolver("xxxxx")


def test_a2fd1cf0():
    runSolver("xxxxx")


def test_a3325580():
    runSolver("xxxxx")


def test_a3df8b1e():
    runSolver("xxxxx")


def test_a416b8f3():
    runSolver("xxxxx")


def test_a48eeaf7():
    runSolver("xxxxx")


def test_a5313dff():
    runSolver("xxxxx")


def test_a5f85a15():
    runSolver("xxxxx")


def test_a61ba2ce():
    runSolver("xxxxx")


def test_a61f2674():
    runSolver("xxxxx")


def test_a64e4611():
    runSolver("xxxxx")


def test_a65b410d():
    runSolver("xxxxx")


def test_a68b268e():
    runSolver("xxxxx")


def test_a699fb00():
    runSolver("xxxxx")


def test_a740d043():
    runSolver("xxxxx")


def test_a78176bb():
    runSolver("xxxxx")


def test_a79310a0():
    runSolver("xxxxx")


def test_a85d4709():
    runSolver("xxxxx")


def test_a87f7484():
    runSolver("xxxxx")


def test_a8c38be5():
    runSolver("xxxxx")


def test_a8d7556c():
    runSolver("xxxxx")


def test_a9f96cdd():
    runSolver("xxxxx")


def test_aabf363d():
    runSolver("xxxxx")


def test_aba27056():
    runSolver("xxxxx")


def test_ac0a08a4():
    runSolver("xxxxx")


def test_ae3edfdc():
    runSolver("xxxxx")


def test_ae4f1146():
    runSolver("xxxxx")


def test_aedd82e4():
    runSolver("xxxxx")


def test_af902bf9():
    runSolver("xxxxx")


def test_b0c4d837():
    runSolver("xxxxx")


def test_b190f7f5():
    runSolver("xxxxx")


def test_b1948b0a():
    runSolver("xxxxx")


def test_b230c067():
    runSolver("xxxxx")


def test_b27ca6d3():
    runSolver("xxxxx")


def test_b2862040():
    runSolver("xxxxx")


def test_b527c5c6():
    runSolver("xxxxx")


def test_b548a754():
    runSolver("xxxxx")


def test_b60334d2():
    runSolver("xxxxx")


def test_b6afb2da():
    runSolver("xxxxx")


def test_b7249182():
    runSolver("xxxxx")


def test_b775ac94():
    runSolver("xxxxx")


def test_b782dc8a():
    runSolver("xxxxx")


def test_b8825c91():
    runSolver("xxxxx")


def test_b8cdaf2b():
    runSolver("xxxxx")


def test_b91ae062():
    runSolver("xxxxx")


def test_b94a9452():
    runSolver("xxxxx")


def test_b9b7f026():
    runSolver("xxxxx")


def test_ba26e723():
    runSolver("xxxxx")


def test_ba97ae07():
    runSolver("xxxxx")


def test_bb43febb():
    runSolver("xxxxx")


def test_bbc9ae5d():
    runSolver("xxxxx")


def test_bc1d5164():
    runSolver("xxxxx")


def test_bd4472b8():
    runSolver("xxxxx")


def test_bda2d7a6():
    runSolver("xxxxx")


def test_bdad9b1f():
    runSolver("xxxxx")


def test_be94b721():
    runSolver("xxxxx")


def test_beb8660c():
    runSolver("xxxxx")


def test_c0f76784():
    runSolver("xxxxx")


def test_c1d99e64():
    runSolver("xxxxx")


def test_c3e719e8():
    runSolver("xxxxx")


def test_c3f564a4():
    runSolver("xxxxx")


def test_c444b776():
    runSolver("xxxxx")


def test_c59eb873():
    runSolver("xxxxx")


def test_c8cbb738():
    runSolver("xxxxx")


def test_c8f0f002():
    runSolver("xxxxx")


def test_c909285e():
    runSolver("xxxxx")


def test_c9e6f938():
    runSolver("xxxxx")


def test_c9f8e694():
    runSolver("xxxxx")


def test_caa06a1f():
    runSolver("xxxxx")


def test_cbded52d():
    runSolver("xxxxx")


def test_cce03e0d():
    runSolver("xxxxx")


def test_cdecee7f():
    runSolver("xxxxx")


def test_ce22a75a():
    runSolver("xxxxx")


def test_ce4f8723():
    runSolver("xxxxx")


def test_ce602527():
    runSolver("xxxxx")


def test_ce9e57f2():
    runSolver("xxxxx")


def test_cf98881b():
    runSolver("xxxxx")


def test_d037b0a7():
    runSolver("xxxxx")


def test_d06dbe63():
    runSolver("xxxxx")


def test_d07ae81c():
    runSolver("xxxxx")


def test_d0f5fe59():
    runSolver("xxxxx")


def test_d10ecb37():
    runSolver("xxxxx")


def test_d13f3404():
    runSolver("xxxxx")


def test_d22278a0():
    runSolver("xxxxx")


def test_d23f8c26():
    runSolver("xxxxx")


def test_d2abd087():
    runSolver("xxxxx")


def test_d364b489():
    runSolver("xxxxx")


def test_d406998b():
    runSolver("xxxxx")


def test_d43fd935():
    runSolver("xxxxx")


def test_d4469b4b():
    runSolver("xxxxx")


def test_d4a91cb9():
    runSolver("xxxxx")


def test_d4f3cd78():
    runSolver("xxxxx")


def test_d511f180():
    runSolver("xxxxx")


def test_d5d6de2d():
    runSolver("xxxxx")


def test_d631b094():
    runSolver("xxxxx")


def test_d687bc17():
    runSolver("xxxxx")


def test_d6ad076f():
    runSolver("xxxxx")


def test_d89b689b():
    runSolver("xxxxx")


def test_d8c310e9():
    runSolver("xxxxx")


def test_d90796e8():
    runSolver("xxxxx")


def test_d9f24cd1():
    runSolver("xxxxx")


def test_d9fac9be():
    runSolver("xxxxx")


def test_dae9d2b5():
    runSolver("xxxxx")


def test_db3e9e38():
    runSolver("xxxxx")


def test_db93a21d():
    runSolver("xxxxx")


def test_dbc1a6ce():
    runSolver("xxxxx")


def test_dc0a314f():
    runSolver("xxxxx")


def test_dc1df850():
    runSolver("xxxxx")


def test_dc433765():
    runSolver("xxxxx")


def test_ddf7fa4f():
    runSolver("xxxxx")


def test_de1cd16c():
    runSolver("xxxxx")


def test_ded97339():
    runSolver("xxxxx")


def test_e179c5f4():
    runSolver("xxxxx")


def test_e21d9049():
    runSolver("xxxxx")


def test_e26a3af2():
    runSolver("xxxxx")


def test_e3497940():
    runSolver("xxxxx")


def test_e40b9e2f():
    runSolver("xxxxx")


def test_e48d4e1a():
    runSolver("xxxxx")


def test_e5062a87():
    runSolver("xxxxx")


def test_e509e548():
    runSolver("xxxxx")


def test_e50d258f():
    runSolver("xxxxx")


def test_e6721834():
    runSolver("xxxxx")


def test_e73095fd():
    runSolver("xxxxx")


def test_e76a88a6():
    runSolver("xxxxx")


def test_e8593010():
    runSolver("xxxxx")


def test_e8dc4411():
    runSolver("xxxxx")


def test_e9614598():
    runSolver("xxxxx")


def test_e98196ab():
    runSolver("xxxxx")


def test_e9afcf9a():
    runSolver("xxxxx")


def test_ea32f347():
    runSolver("xxxxx")


def test_ea786f4a():
    runSolver("xxxxx")


def test_eb281b96():
    runSolver("xxxxx")


def test_eb5a1d5d():
    runSolver("xxxxx")


def test_ec883f72():
    runSolver("xxxxx")


def test_ecdecbb3():
    runSolver("xxxxx")


def test_ed36ccf7():
    runSolver("xxxxx")


def test_ef135b50():
    runSolver("xxxxx")


def test_f15e1fac():
    runSolver("xxxxx")


def test_f1cefba8():
    runSolver("xxxxx")


def test_f25fbde4():
    runSolver("xxxxx")


def test_f25ffba3():
    runSolver("xxxxx")


def test_f2829549():
    runSolver("xxxxx")


def test_f35d900a():
    runSolver("xxxxx")


def test_f5b8619d():
    runSolver("xxxxx")


def test_f76d97a5():
    runSolver("xxxxx")


def test_f8a8fe49():
    runSolver("xxxxx")


def test_f8b3ba0a():
    runSolver("f8b3ba0a")


def test_f8c80d96():
    runSolver("f8c80d96")


def test_f8ff0b80():
    runSolver("f8ff0b80")


def test_f9012d9b():
    runSolver("f9012d9b")


def test_fafffa47():
    runSolver("fafffa47")


def test_fcb5c309():
    runSolver("fcb5c309")


def test_fcc82909():
    runSolver("fcc82909")


def test_feca6190():
    runSolver("feca6190")


def test_ff28f65a():
    runSolver("ff28f65a")


def test_ff805c23():
    runSolver("ff805c23")
