from pamir_cuas_field.tsms import parse_source_file, align_by_index


def test_parse_sequential_index():
    r = parse_source_file("Inspire 2_2m_001.mat", "CW_RADAR", "Inspire 2", 2)
    assert r.sample_index == 1
    assert r.representation == "MEASUREMENT"


def test_alignment_uses_common_index_only():
    a=[parse_source_file(f"A_2m_{i:03}.mat","CW_RADAR","A",2) for i in (1,2)]
    b=[parse_source_file(f"A_2m_{i:03}.mat","RF_RECEIVER","A",2) for i in (2,3)]
    aligned=align_by_index(a,b)
    assert len(aligned)==1 and aligned[0][0].sample_index==2
