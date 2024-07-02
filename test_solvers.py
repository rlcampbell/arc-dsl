import json

from solvers import *


with open("arc-agi_training_challenges.json") as fp:
    train_challenges = json.load(fp)


def runSolver(key):
    task = train_challenges[key]
    train_inputs = [example["input"] for example in task["train"]]
    train_outputs = [example["output"] for example in task["train"]]
    solverFunction = globals()["solve_" + key]
    for i in range(len(train_inputs)):
        trainIn = train_inputs[i]
        trainIn = tuple(tuple(row) for row in trainIn)
        trainOut = train_outputs[i]
        solverOut = solverFunction(trainIn)
        solverOut = [list(inner_tuple) for inner_tuple in solverOut]
        assert solverOut == trainOut


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
    runSolver("09629e4f")


def test_0962bcdd():
    runSolver("0962bcdd")


def test_0a938d79():
    runSolver("0a938d79")


def test_0b148d64():
    runSolver("0b148d64")


def test_0ca9ddb6():
    runSolver("0ca9ddb6")


def test_0d3d703e():
    runSolver("0d3d703e")


def test_0dfd9992():
    runSolver("0dfd9992")


def test_0e206a2e():
    runSolver("0e206a2e")


def test_10fcaaa3():
    runSolver("10fcaaa3")


def test_11852cab():
    runSolver("11852cab")


def test_1190e5a7():
    runSolver("1190e5a7")


def test_137eaa0f():
    runSolver("137eaa0f")


def test_150deff5():
    runSolver("150deff5")


def test_178fcbfb():
    runSolver("178fcbfb")


def test_1a07d186():
    runSolver("1a07d186")


def test_1b2d62fb():
    runSolver("1b2d62fb")


def test_1b60fb0c():
    runSolver("1b60fb0c")


def test_1bfc4729():
    runSolver("1bfc4729")


def test_1c786137():
    runSolver("1c786137")


def test_1caeab9d():
    runSolver("1caeab9d")


def test_1cf80156():
    runSolver("1cf80156")


def test_1e0a9b12():
    runSolver("1e0a9b12")


def test_1e32b0e9():
    runSolver("1e32b0e9")


def test_1f0c79e5():
    runSolver("1f0c79e5")


def test_1f642eb9():
    runSolver("1f642eb9")


def test_1f85a75f():
    runSolver("1f85a75f")


def test_1f876c06():
    runSolver("1f876c06")


def test_1fad071e():
    runSolver("1fad071e")


def test_2013d3e2():
    runSolver("2013d3e2")


def test_2204b7a8():
    runSolver("2204b7a8")


def test_22168020():
    runSolver("22168020")


def test_22233c11():
    runSolver("22233c11")


def test_2281f1f4():
    runSolver("2281f1f4")


def test_228f6490():
    runSolver("228f6490")


def test_22eb0ac0():
    runSolver("22eb0ac0")


def test_234bbc79():
    runSolver("234bbc79")


def test_23581191():
    runSolver("23581191")


def test_239be575():
    runSolver("239be575")


def test_23b5c85d():
    runSolver("23b5c85d")


def test_253bf280():
    runSolver("253bf280")


def test_25d487eb():
    runSolver("25d487eb")


def test_25d8a9c8():
    runSolver("25d8a9c8")


def test_25ff71a9():
    runSolver("25ff71a9")


def test_264363fd():
    runSolver("264363fd")


def test_272f95fa():
    runSolver("272f95fa")


def test_27a28665():
    runSolver("27a28665")


def test_28bf18c6():
    runSolver("28bf18c6")


def test_28e73c20():
    runSolver("28e73c20")


def test_29623171():
    runSolver("29623171")


def test_29c11459():
    runSolver("29c11459")


def test_29ec7d0e():
    runSolver("29ec7d0e")


def test_2bcee788():
    runSolver("2bcee788")


def test_2bee17df():
    runSolver("2bee17df")


def test_2c608aff():
    runSolver("2c608aff")


def test_2dc579da():
    runSolver("2dc579da")


def test_2dd70a9a():
    runSolver("2dd70a9a")


def test_2dee498d():
    runSolver("2dee498d")


def test_31aa019c():
    runSolver("31aa019c")


def test_321b1fc6():
    runSolver("321b1fc6")


def test_32597951():
    runSolver("32597951")


def test_3345333e():
    runSolver("3345333e")


def test_3428a4f5():
    runSolver("3428a4f5")


def test_3618c87e():
    runSolver("3618c87e")


def test_3631a71a():
    runSolver("3631a71a")


def test_363442ee():
    runSolver("363442ee")


def test_36d67576():
    runSolver("36d67576")


def test_36fdfd69():
    runSolver("36fdfd69")


def test_3906de3d():
    runSolver("3906de3d")


def test_39a8645d():
    runSolver("39a8645d")


def test_39e1d7f9():
    runSolver("39e1d7f9")


def test_3aa6fb7a():
    runSolver("3aa6fb7a")


def test_3ac3eb23():
    runSolver("3ac3eb23")


def test_3af2c5a8():
    runSolver("3af2c5a8")


def test_3bd67248():
    runSolver("3bd67248")


def test_3bdb4ada():
    runSolver("3bdb4ada")


def test_3befdf3e():
    runSolver("3befdf3e")


def test_3c9b0459():
    runSolver("3c9b0459")


def test_3de23699():
    runSolver("3de23699")


def test_3e980e27():
    runSolver("3e980e27")


def test_3eda0437():
    runSolver("3eda0437")


def test_3f7978a0():
    runSolver("3f7978a0")


def test_40853293():
    runSolver("40853293")


def test_4093f84a():
    runSolver("4093f84a")


def test_41e4d17e():
    runSolver("41e4d17e")


def test_4258a5f9():
    runSolver("4258a5f9")


def test_4290ef0e():
    runSolver("4290ef0e")


def test_42a50994():
    runSolver("42a50994")


def test_4347f46a():
    runSolver("4347f46a")


def test_444801d8():
    runSolver("444801d8")


def test_445eab21():
    runSolver("445eab21")


def test_447fd412():
    runSolver("447fd412")


def test_44d8ac46():
    runSolver("44d8ac46")


def test_44f52bb0():
    runSolver("44f52bb0")


def test_4522001f():
    runSolver("4522001f")


def test_4612dd53():
    runSolver("4612dd53")


def test_46442a0e():
    runSolver("46442a0e")


def test_469497ad():
    runSolver("469497ad")


def test_46f33fce():
    runSolver("46f33fce")


def test_47c1f68c():
    runSolver("47c1f68c")


def test_484b58aa():
    runSolver("484b58aa")


def test_48d8fb45():
    runSolver("48d8fb45")


def test_4938f0c2():
    runSolver("4938f0c2")


def test_496994bd():
    runSolver("496994bd")


def test_49d1d64f():
    runSolver("49d1d64f")


def test_4be741c5():
    runSolver("4be741c5")


def test_4c4377d9():
    runSolver("4c4377d9")


def test_4c5c2cf0():
    runSolver("4c5c2cf0")


def test_50846271():
    runSolver("50846271")


def test_508bd3b6():
    runSolver("508bd3b6")


def test_50cb2852():
    runSolver("50cb2852")


def test_5117e062():
    runSolver("5117e062")


def test_5168d44c():
    runSolver("5168d44c")


def test_539a4f51():
    runSolver("539a4f51")


def test_53b68214():
    runSolver("53b68214")


def test_543a7ed5():
    runSolver("543a7ed5")


def test_54d82841():
    runSolver("54d82841")


def test_54d9e175():
    runSolver("54d9e175")


def test_5521c0d9():
    runSolver("5521c0d9")


def test_5582e5ca():
    runSolver("5582e5ca")


def test_5614dbcf():
    runSolver("5614dbcf")


def test_56dc2b01():
    runSolver("56dc2b01")


def test_56ff96f3():
    runSolver("56ff96f3")


def test_57aa92db():
    runSolver("57aa92db")


def test_5ad4f10b():
    runSolver("5ad4f10b")


def test_5bd6f4ac():
    runSolver("5bd6f4ac")


def test_5c0a986e():
    runSolver("5c0a986e")


def test_5c2c9af4():
    runSolver("5c2c9af4")


def test_5daaa586():
    runSolver("5daaa586")


def test_60b61512():
    runSolver("60b61512")


def test_6150a2bd():
    runSolver("6150a2bd")


def test_623ea044():
    runSolver("623ea044")


def test_62c24649():
    runSolver("62c24649")


def test_63613498():
    runSolver("63613498")


def test_6430c8c4():
    runSolver("6430c8c4")


def test_6455b5f5():
    runSolver("6455b5f5")


def test_662c240a():
    runSolver("662c240a")


def test_67385a82():
    runSolver("67385a82")


def test_673ef223():
    runSolver("673ef223")


def test_6773b310():
    runSolver("6773b310")


def test_67a3c6ac():
    runSolver("67a3c6ac")


def test_67a423a3():
    runSolver("67a423a3")


def test_67e8384a():
    runSolver("67e8384a")


def test_681b3aeb():
    runSolver("681b3aeb")


def test_6855a6e4():
    runSolver("6855a6e4")


def test_68b16354():
    runSolver("68b16354")


def test_694f12f3():
    runSolver("694f12f3")


def test_6a1e5592():
    runSolver("6a1e5592")


def test_6aa20dc0():
    runSolver("6aa20dc0")


def test_6b9890af():
    runSolver("6b9890af")


def test_6c434453():
    runSolver("6c434453")


def test_6cdd2623():
    runSolver("6cdd2623")


def test_6cf79266():
    runSolver("6cf79266")


def test_6d0160f0():
    runSolver("6d0160f0")


def test_6d0aefbc():
    runSolver("6d0aefbc")


def test_6d58a25d():
    runSolver("6d58a25d")


def test_6d75e8bb():
    runSolver("6d75e8bb")


def test_6e02f1e3():
    runSolver("6e02f1e3")


def test_6e19193c():
    runSolver("6e19193c")


def test_6e82a1ae():
    runSolver("6e82a1ae")


def test_6ecd11f4():
    runSolver("6ecd11f4")


def test_6f8cd79b():
    runSolver("6f8cd79b")


def test_6fa7a44f():
    runSolver("6fa7a44f")


def test_72322fa7():
    runSolver("72322fa7")


def test_72ca375d():
    runSolver("72ca375d")


def test_73251a56():
    runSolver("73251a56")


def test_7447852a():
    runSolver("7447852a")


def test_7468f01a():
    runSolver("7468f01a")


def test_746b3537():
    runSolver("746b3537")


def test_74dd1130():
    runSolver("74dd1130")


def test_75b8110e():
    runSolver("75b8110e")


def test_760b3cac():
    runSolver("760b3cac")


def test_776ffc46():
    runSolver("776ffc46")


def test_77fdfe62():
    runSolver("77fdfe62")


def test_780d0b14():
    runSolver("780d0b14")


def test_7837ac64():
    runSolver("7837ac64")


def test_794b24be():
    runSolver("794b24be")


def test_7b6016b9():
    runSolver("7b6016b9")


def test_7b7f7511():
    runSolver("7b7f7511")


def test_7c008303():
    runSolver("7c008303")


def test_7ddcd7ec():
    runSolver("7ddcd7ec")


def test_7df24a62():
    runSolver("7df24a62")


def test_7e0986d6():
    runSolver("7e0986d6")


def test_7f4411dc():
    runSolver("7f4411dc")


def test_7fe24cdd():
    runSolver("7fe24cdd")


def test_80af3007():
    runSolver("80af3007")


def test_810b9b61():
    runSolver("810b9b61")


def test_82819916():
    runSolver("82819916")


def test_83302e8f():
    runSolver("83302e8f")


def test_834ec97d():
    runSolver("834ec97d")


def test_8403a5d5():
    runSolver("8403a5d5")


def test_846bdb03():
    runSolver("846bdb03")


def test_855e0971():
    runSolver("855e0971")


def test_85c4e7cd():
    runSolver("85c4e7cd")


def test_868de0fa():
    runSolver("868de0fa")


def test_8731374e():
    runSolver("8731374e")


def test_88a10436():
    runSolver("88a10436")


def test_88a62173():
    runSolver("88a62173")


def test_890034e9():
    runSolver("890034e9")


def test_8a004b2b():
    runSolver("8a004b2b")


def test_8be77c9e():
    runSolver("8be77c9e")


def test_8d5021e8():
    runSolver("8d5021e8")


def test_8d510a79():
    runSolver("8d510a79")


def test_8e1813be():
    runSolver("8e1813be")


def test_8e5a5113():
    runSolver("8e5a5113")


def test_8eb1be9a():
    runSolver("8eb1be9a")


def test_8efcae92():
    runSolver("8efcae92")


def test_8f2ea7aa():
    runSolver("8f2ea7aa")


def test_90c28cc7():
    runSolver("90c28cc7")


def test_90f3ed37():
    runSolver("90f3ed37")


def test_913fb3ed():
    runSolver("913fb3ed")


def test_91413438():
    runSolver("91413438")


def test_91714a58():
    runSolver("91714a58")


def test_9172f3a0():
    runSolver("9172f3a0")


def test_928ad970():
    runSolver("928ad970")


def test_93b581b8():
    runSolver("93b581b8")


def test_941d9a10():
    runSolver("941d9a10")


def test_94f9d214():
    runSolver("94f9d214")


def test_952a094c():
    runSolver("952a094c")


def test_9565186b():
    runSolver("9565186b")


def test_95990924():
    runSolver("95990924")


def test_963e52fc():
    runSolver("963e52fc")


def test_97999447():
    runSolver("97999447")


def test_97a05b5b():
    runSolver("97a05b5b")


def test_98cf29f8():
    runSolver("98cf29f8")


def test_995c5fa3():
    runSolver("995c5fa3")


def test_99b1bc43():
    runSolver("99b1bc43")


def test_99fa7670():
    runSolver("99fa7670")


def test_9aec4887():
    runSolver("9aec4887")


def test_9af7a82c():
    runSolver("9af7a82c")


def test_9d9215db():
    runSolver("9d9215db")


def test_9dfd6313():
    runSolver("9dfd6313")


def test_9ecd008a():
    runSolver("9ecd008a")


def test_9edfc990():
    runSolver("9edfc990")


def test_9f236235():
    runSolver("9f236235")


def test_a1570a43():
    runSolver("a1570a43")


def test_a2fd1cf0():
    runSolver("a2fd1cf0")


def test_a3325580():
    runSolver("a3325580")


def test_a3df8b1e():
    runSolver("a3df8b1e")


def test_a416b8f3():
    runSolver("a416b8f3")


def test_a48eeaf7():
    runSolver("a48eeaf7")


def test_a5313dff():
    runSolver("a5313dff")


def test_a5f85a15():
    runSolver("a5f85a15")


def test_a61ba2ce():
    runSolver("a61ba2ce")


def test_a61f2674():
    runSolver("a61f2674")


def test_a64e4611():
    runSolver("a64e4611")


def test_a65b410d():
    runSolver("a65b410d")


def test_a68b268e():
    runSolver("a68b268e")


def test_a699fb00():
    runSolver("a699fb00")


def test_a740d043():
    runSolver("a740d043")


def test_a78176bb():
    runSolver("a78176bb")


def test_a79310a0():
    runSolver("a79310a0")


def test_a85d4709():
    runSolver("a85d4709")


def test_a87f7484():
    runSolver("a87f7484")


def test_a8c38be5():
    runSolver("a8c38be5")


def test_a8d7556c():
    runSolver("a8d7556c")


def test_a9f96cdd():
    runSolver("a9f96cdd")


def test_aabf363d():
    runSolver("aabf363d")


def test_aba27056():
    runSolver("aba27056")


def test_ac0a08a4():
    runSolver("ac0a08a4")


def test_ae3edfdc():
    runSolver("ae3edfdc")


def test_ae4f1146():
    runSolver("ae4f1146")


def test_aedd82e4():
    runSolver("aedd82e4")


def test_af902bf9():
    runSolver("af902bf9")


def test_b0c4d837():
    runSolver("b0c4d837")


def test_b190f7f5():
    runSolver("b190f7f5")


def test_b1948b0a():
    runSolver("b1948b0a")


def test_b230c067():
    runSolver("b230c067")


def test_b27ca6d3():
    runSolver("b27ca6d3")


def test_b2862040():
    runSolver("b2862040")


def test_b527c5c6():
    runSolver("b527c5c6")


def test_b548a754():
    runSolver("b548a754")


def test_b60334d2():
    runSolver("b60334d2")


def test_b6afb2da():
    runSolver("b6afb2da")


def test_b7249182():
    runSolver("b7249182")


def test_b775ac94():
    runSolver("b775ac94")


def test_b782dc8a():
    runSolver("b782dc8a")


def test_b8825c91():
    runSolver("b8825c91")


def test_b8cdaf2b():
    runSolver("b8cdaf2b")


def test_b91ae062():
    runSolver("b91ae062")


def test_b94a9452():
    runSolver("b94a9452")


def test_b9b7f026():
    runSolver("b9b7f026")


def test_ba26e723():
    runSolver("ba26e723")


def test_ba97ae07():
    runSolver("ba97ae07")


def test_bb43febb():
    runSolver("bb43febb")


def test_bbc9ae5d():
    runSolver("bbc9ae5d")


def test_bc1d5164():
    runSolver("bc1d5164")


def test_bd4472b8():
    runSolver("bd4472b8")


def test_bda2d7a6():
    runSolver("bda2d7a6")


def test_bdad9b1f():
    runSolver("bdad9b1f")


def test_be94b721():
    runSolver("be94b721")


def test_beb8660c():
    runSolver("beb8660c")


def test_c0f76784():
    runSolver("c0f76784")


def test_c1d99e64():
    runSolver("c1d99e64")


def test_c3e719e8():
    runSolver("c3e719e8")


def test_c3f564a4():
    runSolver("c3f564a4")


def test_c444b776():
    runSolver("c444b776")


def test_c59eb873():
    runSolver("c59eb873")


def test_c8cbb738():
    runSolver("c8cbb738")


def test_c8f0f002():
    runSolver("c8f0f002")


def test_c909285e():
    runSolver("c909285e")


def test_c9e6f938():
    runSolver("c9e6f938")


def test_c9f8e694():
    runSolver("c9f8e694")


def test_caa06a1f():
    runSolver("caa06a1f")


def test_cbded52d():
    runSolver("cbded52d")


def test_cce03e0d():
    runSolver("cce03e0d")


def test_cdecee7f():
    runSolver("cdecee7f")


def test_ce22a75a():
    runSolver("ce22a75a")


def test_ce4f8723():
    runSolver("ce4f8723")


def test_ce602527():
    runSolver("ce602527")


def test_ce9e57f2():
    runSolver("ce9e57f2")


def test_cf98881b():
    runSolver("cf98881b")


def test_d037b0a7():
    runSolver("d037b0a7")


def test_d06dbe63():
    runSolver("d06dbe63")


def test_d07ae81c():
    runSolver("d07ae81c")


def test_d0f5fe59():
    runSolver("d0f5fe59")


def test_d10ecb37():
    runSolver("d10ecb37")


def test_d13f3404():
    runSolver("d13f3404")


def test_d22278a0():
    runSolver("d22278a0")


def test_d23f8c26():
    runSolver("d23f8c26")


def test_d2abd087():
    runSolver("d2abd087")


def test_d364b489():
    runSolver("d364b489")


def test_d406998b():
    runSolver("d406998b")


def test_d43fd935():
    runSolver("d43fd935")


def test_d4469b4b():
    runSolver("d4469b4b")


def test_d4a91cb9():
    runSolver("d4a91cb9")


def test_d4f3cd78():
    runSolver("d4f3cd78")


def test_d511f180():
    runSolver("d511f180")


def test_d5d6de2d():
    runSolver("d5d6de2d")


def test_d631b094():
    runSolver("d631b094")


def test_d687bc17():
    runSolver("d687bc17")


def test_d6ad076f():
    runSolver("d6ad076f")


def test_d89b689b():
    runSolver("d89b689b")


def test_d8c310e9():
    runSolver("d8c310e9")


def test_d90796e8():
    runSolver("d90796e8")


def test_d9f24cd1():
    runSolver("d9f24cd1")


def test_d9fac9be():
    runSolver("d9fac9be")


def test_dae9d2b5():
    runSolver("dae9d2b5")


def test_db3e9e38():
    runSolver("db3e9e38")


def test_db93a21d():
    runSolver("db93a21d")


def test_dbc1a6ce():
    runSolver("dbc1a6ce")


def test_dc0a314f():
    runSolver("dc0a314f")


def test_dc1df850():
    runSolver("dc1df850")


def test_dc433765():
    runSolver("dc433765")


def test_ddf7fa4f():
    runSolver("ddf7fa4f")


def test_de1cd16c():
    runSolver("de1cd16c")


def test_ded97339():
    runSolver("ded97339")


def test_e179c5f4():
    runSolver("e179c5f4")


def test_e21d9049():
    runSolver("e21d9049")


def test_e26a3af2():
    runSolver("e26a3af2")


def test_e3497940():
    runSolver("e3497940")


def test_e40b9e2f():
    runSolver("e40b9e2f")


def test_e48d4e1a():
    runSolver("e48d4e1a")


def test_e5062a87():
    runSolver("e5062a87")


def test_e509e548():
    runSolver("e509e548")


def test_e50d258f():
    runSolver("e50d258f")


def test_e6721834():
    runSolver("e6721834")


def test_e73095fd():
    runSolver("e73095fd")


def test_e76a88a6():
    runSolver("e76a88a6")


def test_e8593010():
    runSolver("e8593010")


def test_e8dc4411():
    runSolver("e8dc4411")


def test_e9614598():
    runSolver("e9614598")


def test_e98196ab():
    runSolver("e98196ab")


def test_e9afcf9a():
    runSolver("e9afcf9a")


def test_ea32f347():
    runSolver("ea32f347")


def test_ea786f4a():
    runSolver("ea786f4a")


def test_eb281b96():
    runSolver("eb281b96")


def test_eb5a1d5d():
    runSolver("eb5a1d5d")


def test_ec883f72():
    runSolver("ec883f72")


def test_ecdecbb3():
    runSolver("ecdecbb3")


def test_ed36ccf7():
    runSolver("ed36ccf7")


def test_ef135b50():
    runSolver("ef135b50")


def test_f15e1fac():
    runSolver("f15e1fac")


def test_f1cefba8():
    runSolver("f1cefba8")


def test_f25fbde4():
    runSolver("f25fbde4")


def test_f25ffba3():
    runSolver("f25ffba3")


def test_f2829549():
    runSolver("f2829549")


def test_f35d900a():
    runSolver("f35d900a")


def test_f5b8619d():
    runSolver("f5b8619d")


def test_f76d97a5():
    runSolver("f76d97a5")


def test_f8a8fe49():
    runSolver("f8a8fe49")


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
