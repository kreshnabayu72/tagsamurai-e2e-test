---
id: TC-FA-TAG-E2E-247-tabel-to-be-returned-filter-per-kolom-dan-kombinasi-bagian-2
title: "Tabel To Be Returned: Cancel Tree Picker, Filter Current Holder, Since Inklusif, dan Kombinasi Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-997
  - TC-FA-TAG-998
  - TC-FA-TAG-999
  - TC-FA-TAG-1000
  - TC-FA-TAG-1001
coverage:
  web: automated
---

# Tabel To Be Returned: Cancel Tree Picker, Filter Current Holder, Since Inklusif, dan Kombinasi Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned (kunci `Fixture.fixedAssetTag.tbr4`; tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah; tabel To Be Returned dalam scope akun berisi tepat empat Tag ini; Return Group 'Disposal Center' berada di bawah group induk 'Operations'):

| TAG Code | Last Asset | Reason | Return Group | Current Holder | Since |
|---|---|---|---|---|---|
| RF-00071 (RFID) | Excavator 20 Ton - 2 | Disposal | Disposal Center | Dedi K. | 01 Sep 2026 |
| RF-00088 (RFID) | Excavator 20 Ton - 5 | Disposal | Disposal Center | Dedi K. | 20 Sep 2026 |
| NF-00092 (NFC) | Laptop Pro 14 - 8 | Disposal | HQ Warehouse | Rina T. | 22 Sep 2026 |
| RF-00110 (RFID) | Excavator 20 Ton - 10 | Disposal | Disposal Center | Dedi K. | 10 Sep 2026 |

- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Filter dikosongkan di akhir tiap kasus.

## Test Steps

### TC-FA-TAG-997: Cancel pada Modal Tree Picker

1. Klik tab `To Be Returned`
2. Klik ikon Filter
3. Klik field "Return Group"
4. Centang node "HQ Warehouse"
5. Klik [Cancel]
6. Verifikasi Modal Tree Picker menutup
7. Verifikasi field "Return Group" tetap kosong

### TC-FA-TAG-998: Filter Current Holder

8. Buka daftar opsi field "Current Holder"
9. Verifikasi opsi pada field hanya "Dedi K." dan "Rina T."
10. Pilih opsi "Dedi K." pada field "Current Holder"
11. Klik [Apply]
12. Verifikasi tabel menampilkan RF-00071, RF-00088, dan RF-00110
13. Verifikasi NF-00092 tidak tampil
14. Klik [Clear Field]
15. Klik [Apply]

### TC-FA-TAG-999: Filter Since inklusif di kedua ujung

16. Pilih rentang tanggal 01 Sep 2026 sampai 20 Sep 2026 pada field "Since"
17. Klik [Apply]
18. Verifikasi tabel menampilkan RF-00071 (01 Sep), RF-00110 (10 Sep), dan RF-00088 (20 Sep)
19. Verifikasi NF-00092 (22 Sep) tidak tampil
20. Klik [Clear Field]
21. Klik [Apply]

### TC-FA-TAG-1000: dua filter digabung dengan AND

22. Pilih "RFID" pada "TAG Type" dan "Dedi K." pada "Current Holder"
23. Klik [Apply]
24. Verifikasi tabel menampilkan RF-00071, RF-00088, dan RF-00110
25. Klik [Clear Field]
26. Klik [Apply]

### TC-FA-TAG-1001: kombinasi filter tanpa hasil

27. Pilih "NFC" pada "TAG Type" dan "Dedi K." pada "Current Holder"
28. Klik [Apply]
29. Verifikasi tabel menampilkan ilustrasi, judul "No results found", dan deskripsi "Try adjusting your search or filter."
30. Klik [Clear Field]
31. Klik [Apply]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-997 s.d. 1001). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-992 s.d. 996 ada di spec 246 dan TC-FA-TAG-1002 s.d. 1004 ada di spec 248.
- Urutan TC mengikuti nomor TC. TC-FA-TAG-997 (Cancel, tanpa perubahan) berada di awal sebelum kasus yang menerapkan Filter.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 14, 20, 25, 30 (mengosongkan Filter lewat [Clear Field]); 15, 21, 26, 31 (menerapkan Filter kosong lewat [Apply]).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-998 Expected butir b (opsi hanya "Dedi K." dan "Rina T.") tidak menyebut kapan daftar dibuka; spec membuka daftar sebelum memilih opsi dan memverifikasinya lebih dulu.
  - TC-FA-TAG-999 Expected menyebut tanggal Since tiap Tag tanpa menyebut format tampil kolom Since; spec memakai tanggal seperti di TC.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
