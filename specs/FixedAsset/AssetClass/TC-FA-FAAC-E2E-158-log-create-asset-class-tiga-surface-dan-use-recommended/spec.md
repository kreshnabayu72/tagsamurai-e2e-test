---
id: TC-FA-FAAC-E2E-158-log-create-asset-class-tiga-surface-dan-use-recommended
title: "Log Create Asset Class pada Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-526
  - TC-FA-FAAC-527
coverage:
  web: automated
---

# Log Create Asset Class pada Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): tabel Asset Class kosong (state client dikosongkan lewat fixture BE di hook `before`); Tax Depreciation Class rekomendasi berstatus Active sehingga EmptyState menampilkan link `Use recommended classes`. Nilai field wajib Create `B-LOG1` mengikuti fixture.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Asset Class BLDG, LAND, dan B-LOG1 dihapus dan tabel Asset Class dikembalikan ke keadaan seed Pre-setup.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-527: Log Create pada Use Recommended Classes satu kejadian per Asset Class

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Klik link `Use recommended classes` pada EmptyState tabel Asset Class
3. Pilih hanya BLDG dan LAND pada dialog Use Recommended Classes, lalu klik `Create`
4. Tunggu aksi selesai
5. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
6. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
7. Verifikasi baris Changelog untuk BLDG: Action `Create`, Field `Class Code`, Old Value `—`, New Value `BLDG`
8. Verifikasi baris Changelog untuk LAND: Action `Create`, Field `Class Code`, Old Value `—`, New Value `LAND`
9. Tutup modal Changelog
10. Buka Global Settings > User > Detail User milik aktor > Tab System Log
11. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
12. Verifikasi baris System Log untuk BLDG: Action `Create`, Object `Asset Class`, Name `BLDG`, Field `Class Code`, Old Value `—`, New Value `BLDG`
13. Verifikasi baris System Log untuk LAND: Action `Create`, Object `Asset Class`, Name `LAND`, Field `Class Code`, Old Value `—`, New Value `LAND`
14. Buka Activity Log FAMS
15. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
16. Verifikasi baris Activity Log untuk BLDG: Object `Asset Class`, Name `BLDG`, Modified By `Rina W`
17. Verifikasi baris Activity Log untuk LAND: Object `Asset Class`, Name `LAND`, Modified By `Rina W`

### TC-FA-FAAC-526: Log Create Asset Class pada tiga surface

18. Buka Fixed Asset > Settings > Accounting > tab Asset Class
19. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
20. Klik `+ Asset Class`, isi semua field wajib dengan nilai valid dan Class Code `B-LOG1`, lalu klik `Submit`
21. Tunggu aksi selesai
22. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
23. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc (tepat satu entri: tidak ada entri ganda dan tidak ada entri untuk field lain)
24. Verifikasi baris teratas Changelog: Action `Create`, Class Code `B-LOG1`, Field `Class Code`, Old Value `—`, New Value `B-LOG1`, Modified By `Rina W`
25. Tutup modal Changelog
26. Buka Global Settings > User > Detail User milik aktor > Tab System Log
27. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
28. Verifikasi baris teratas System Log: Action `Create`, Object `Asset Class`, Name `B-LOG1`, Field `Class Code`, Old Value `—`, New Value `B-LOG1`
29. Buka Activity Log FAMS
30. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
31. Verifikasi baris teratas Activity Log: baris yang sama dengan Object `Asset Class`, Name `B-LOG1`, dan Modified By `Rina W`

## Notes

1. Urutan dalam spec: TC-527 lebih dulu karena membutuhkan tabel Asset Class kosong; TC-526 menyusul pada tabel yang sudah berisi BLDG dan LAND. Urutan ini berbeda dari nomor TC.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 19 (baseline log), langkah 18 (kembali ke layar awal sesudah membuka Activity Log, S-14). Membuka Changelog, System Log, dan Activity Log adalah langkah observasi TC. Langkah "Tunggu aksi selesai" (4, 21) sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log (8b butir 8).
3. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Temuan untuk QA: (a) TC-526 menulis "semua field wajib valid" tanpa nilainya; spec memakai nilai fixture. (b) TC-527 tidak menyebut cara memilih BLDG dan LAND di dialog Use Recommended Classes dan label tombol konfirmasinya; spec memakai `Create` seperti spec lain di suite ini. (c) TC-527 butir b (Activity Log) tanpa kolom; spec mengasersi Object, Name, dan Modified By.
