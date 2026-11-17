---
id: TC-FA-FAAC-E2E-093-toggle-status-satu-asset-class-berhasil
title: "Toggle Status Satu Asset Class: Activate dan Deactivate Berhasil"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-294
  - TC-FA-FAAC-296
  - TC-FA-FAAC-297
sourceRules: ["D-08", "ST-31", "T-04", "L-04", "D-01", "T-05a", "ST-01"]
smoke: []
dependsOn: []
trace:
  "D-08": 4
  "ST-31": [4, 7, 18, 27]
  "T-04": 6
  "L-04": [9, 10, 20, 21]
  "D-01": 15
  "T-05a": [17, 26]
  "ST-01": 29
coverage:
  web: automated
---

# Toggle Status Satu Asset Class: Activate dan Deactivate Berhasil

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode literal TC, disediakan tim FE/BE lewat fixture BE): `B-IN7` "Inactive Seven" Inactive; `B-INACT` "Inactive Candidate" Active tanpa Asset Name.
- Changelog dibaca lewat kemampuan baca Changelog yang disediakan tim FE/BE (jumlah entri dicatat sebelum aksi; N tidak diturunkan dari seeding, bagian 8b butir 10).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: status `B-IN7` kembali Inactive dan `B-INACT` kembali Active. Pemulihan `B-INACT` ke Active juga dilakukan sebagai langkah penghubung di antara TC-296 dan TC-297 (kedua TC mulai dari `B-INACT` Active).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-294: Activate satu Asset Class lewat toggle

1. Ketik Search `B-IN7`, tekan Enter
2. Catat jumlah entri Changelog sebagai baseline N
3. Klik toggle kolom Active pada baris `B-IN7` (Off)
4. Verifikasi toggle tidak langsung berubah (tetap Off) dan Dialog `Activate Asset Class` berisi `• B-IN7 – Inactive Seven` dan `Are you sure you want to activate it?` dengan tombol `Cancel` dan `Activate`
5. Klik `Activate`
6. Verifikasi toast sukses `Success, asset class has been activated.`
7. Verifikasi toggle pada baris `B-IN7` menjadi On
8. Buka Changelog
9. Verifikasi jumlah entri Changelog bertambah 1 dari N
10. Verifikasi entri teratas adalah Edit Field `Status` Old `Inactive` New `Active`
11. Tutup modal Changelog

### TC-FA-FAAC-296: Deactivate satu Asset Class tanpa Asset Name lewat toggle

12. Ganti isi kotak search dengan `B-INACT`, tekan Enter
13. Catat jumlah entri Changelog sebagai baseline N
14. Klik toggle kolom Active pada baris `B-INACT` (On)
15. Verifikasi Dialog `Deactivate Asset Class` berisi `• B-INACT – Inactive Candidate` dan `Are you sure you want to deactivate it?` dengan tombol `Cancel` dan `Deactivate` (merah)
16. Klik `Deactivate`
17. Verifikasi toast sukses `Success, asset class has been deactivated.`
18. Verifikasi toggle pada baris `B-INACT` menjadi Off
19. Buka Changelog
20. Verifikasi jumlah entri Changelog bertambah 1 dari N
21. Verifikasi entri teratas adalah Edit Field `Status` Old `Active` New `Inactive`
22. Tutup modal Changelog

### TC-FA-FAAC-297: Deactivate Asset Class tanpa Asset Name hingga berstatus Inactive

23. Pulihkan `B-INACT` ke status Active lewat fixture BE hingga status tersimpan, lalu muat ulang halaman
24. Klik toggle kolom Active pada baris `B-INACT` (On)
25. Klik `Deactivate` pada dialog `Deactivate Asset Class`
26. Verifikasi toast sukses `Success, asset class has been deactivated.`
27. Verifikasi toggle pada baris `B-INACT` Off
28. Buka Detail `B-INACT`
29. Verifikasi Badge Status pada Detail `Inactive`
30. Klik breadcrumb `Asset Class`

31. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: Activate (TC-294), lalu Deactivate (TC-296 dan TC-297) yang mengubah status.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 12 (Search untuk menemukan baris target, R-16), langkah 2 dan 13 (pencatatan baseline Changelog, S-12), langkah 11 dan 22 (menutup modal Changelog), langkah 23 (memulihkan `B-INACT` Active supaya TC-297 mulai dari kondisi TC), langkah 30 (kembali ke tabel), dan langkah 31 (mengosongkan Search). Langkah 8 dan 19 membuka Changelog sebagai langkah observasi karena TC-294 dan TC-296 tidak menuliskan langkah itu padahal Expected memuat Changelog.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Pembagian TC: TC-296 dan TC-297 memakai `B-INACT` yang sama dan keduanya mulai dari status Active, sehingga TC-297 didahului pemulihan di langkah penghubung.
5. Pembagian TC: TC-295 dan TC-298 (batal pada dialog Activate dan Deactivate) ada di spec 111.
6. Temuan untuk QA: Precondition TC-296 dan TC-297 tidak menyebut data seed `B-INACT` (hanya "User berada di Settings > Accounting > Asset Class"); `B-INACT` tanpa Asset Name disediakan tim FE/BE. Post Condition TC-297 ("dipakai TC lain sebagai data populasi") tidak diasersi.
