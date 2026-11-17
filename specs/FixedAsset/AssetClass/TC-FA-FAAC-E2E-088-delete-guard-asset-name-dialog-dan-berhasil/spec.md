---
id: TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil
title: "Delete Guard D-06 Asset Name, Cancel Dialog Delete, dan Delete Berhasil"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-214
  - TC-FA-FAAC-215
  - TC-FA-FAAC-219
  - TC-FA-FAAC-220
  - TC-FA-FAAC-221
sourceRules: ["D-05", "F-FAAC-05.k3", "D-06", "§3.4#p1", "FAAC-LOGIC-12b", "D-07", "T-06", "S-06a", "S-06b", "S-06c"]
smoke: []
dependsOn: []
trace:
  "D-05": 3
  "F-FAAC-05.k3": [3, 4]
  "D-06": [8, 15]
  "§3.4#p1": 10
  "FAAC-LOGIC-12b": 12
  "D-07": 27
  "T-06": 29
  "S-06a": 30
  "S-06b": 31
  "S-06c": 32
anchor: [21, 22, 23, 24]
coverage:
  web: automated
---

# Delete Guard D-06 Asset Name, Cancel Dialog Delete, dan Delete Berhasil

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode literal TC, disediakan tim FE/BE lewat fixture BE): `B-USEDN` "Used With Names" dengan Last Posted Period Mar 2026 dan 3 Asset Name; `B-NAMES` "Names Fixture" dengan 2 Asset Name tanpa aset aktif, belum pernah diposting; `B-ONE` "One Name Fixture" dengan 1 Asset Name; `B-DEL2` tanpa Asset Name, belum pernah diposting; `B-DEL1` "Delete Candidate" Active tanpa Asset Name, belum pernah diposting.
- State yang diubah spec: `B-DEL1` terhapus permanen oleh TC-214. Pemulihan `B-DEL1` dilakukan fixture BE di hook `after` (seed idempotent); Asset Class lain tidak berubah.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-221: Guard 1 dan Guard 2 bersamaan menampilkan D-05 saja

1. Ketik Search `B-USEDN`, tekan Enter
2. Klik ikon `⋯` pada baris `B-USEDN`, lalu pilih `Delete`
3. Verifikasi hanya Dialog D-05 `Cannot Delete Asset Class` dengan `This asset class was used in depreciation for Mar 2026.` yang tampil
4. Verifikasi Dialog D-06 tidak tampil
5. Klik `Cancel`

### TC-FA-FAAC-219: Delete Asset Class yang punya Asset Name (Guard 2) menampilkan D-06

6. Ganti isi kotak search dengan `B-NAMES`, tekan Enter
7. Klik ikon `⋯` pada baris `B-NAMES`, lalu pilih `Delete`
8. Verifikasi Dialog Blok `Cannot Delete Asset Class` berisi `• B-NAMES – Names Fixture` dan `This asset class is used by 2 asset names.` dengan tombol `Cancel` dan `View asset names`
9. Klik `View asset names`
10. Verifikasi Detail `B-NAMES` terbuka pada tab Asset Names
11. Klik breadcrumb `Asset Class`
12. Verifikasi baris `B-NAMES` masih ada di tabel (Asset Class tidak terhapus)

### TC-FA-FAAC-220: Teks D-06 untuk satu Asset Name

13. Ganti isi kotak search dengan `B-ONE`, tekan Enter
14. Klik ikon `⋯` pada baris `B-ONE`, lalu pilih `Delete`
15. Verifikasi teks dialog `This asset class is used by 1 asset name.`
16. Klik `Cancel`

### TC-FA-FAAC-215: Cancel pada dialog Delete tidak menghapus

17. Ganti isi kotak search dengan `B-DEL2`, tekan Enter
18. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
19. Klik ikon `⋯` pada baris `B-DEL2`, lalu pilih `Delete`
20. Klik `Cancel`
21. Verifikasi tidak ada toast yang tampil
22. Verifikasi dialog menutup
23. Verifikasi baris `B-DEL2` tetap ada di tabel
24. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-214: Delete Asset Class yang lolos kedua guard

25. Ganti isi kotak search dengan `B-DEL1`, tekan Enter
26. Klik ikon `⋯` pada baris `B-DEL1`, lalu pilih `Delete`
27. Verifikasi Dialog `Delete Asset Class` berisi `• B-DEL1 – Delete Candidate` dan `This action cannot be undone. Are you sure you want to delete it?` dengan tombol `Cancel` dan `Delete` (merah)
28. Klik `Delete`
29. Verifikasi toast sukses `Success, asset class has been deleted.`
30. Verifikasi baris `B-DEL1` hilang dari tabel dan tidak ada Asset Class dengan kode itu
31. Verifikasi Asset Class `B-DEL1` tidak lagi tampil di dropdown Asset Class
32. Verifikasi Used By akun dihitung ulang
33. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: dialog blokir dan screening lebih dulu (TC-221, TC-219, TC-220), pembatalan (TC-215), dan Delete yang menghapus data di akhir (TC-214).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 6, 13, 17, dan 25 (Search untuk menemukan baris target, R-16), langkah 18 (baseline Changelog, S-12), langkah 5, 16 (menutup dialog), langkah 11 (kembali ke tabel lewat breadcrumb), dan langkah 33 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dan asersi bergantung pada nama dan jumlah Asset Name; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini). Target Delete (`B-DEL1`) adalah baris seed milik spec ini yang dipulihkan fixture BE.
4. S-05 dan P-1: Expected "tanpa log" pada TC-215 diasersi di spec ini (langkah 24) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Temuan untuk QA: TC-214 Expected d ("tidak lagi tampil di dropdown Asset Class" dan "Used By akun dihitung ulang") tidak menyebut lokasi dropdown dan akun mana yang diamati; spec menulis klausa itu apa adanya tanpa langkah observasi tambahan. Post Condition TC-214 ("terhapus permanen") tidak punya langkah observasi sendiri dan tidak diasersi terpisah. Tabel Data Uji Pre-setup TC hanya memuat akun fixture; data seed Asset Class hanya tertulis di Precondition tiap TC.
