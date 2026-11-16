---
id: TC-FA-FAAC-E2E-098-apply-changes-screening-berhasil-dan-batal
title: "Apply Changes: Screening Dialog, Cancel, dan Apply dengan Effective From Bulan Berjalan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-307
  - TC-FA-FAAC-308
  - TC-FA-FAAC-310
sourceRules: ["D-11", "FLD-26", "FAAC-LOGIC-07c", "FAAC-LOGIC-07f", "§4.2d#p1", "§[F-FAAC-02] Edit Asset Class#b4", "E-FAAC-08", "F-FAAC-02.k18", "T-02", "§4.1.1#r4", "§[F-FAAC-02] Edit Asset Class#p2", "ST-34", "FAAC-LOGIC-09d"]
smoke: []
dependsOn: []
trace:
  "D-11": 8
  "FLD-26": 9
  "FAAC-LOGIC-07c": 9
  "FAAC-LOGIC-07f": 10
  "§4.2d#p1": [11, 15]
  "§[F-FAAC-02] Edit Asset Class#b4": 12
  "E-FAAC-08": [14, 16, 17, 18]
  "F-FAAC-02.k18": [21, 22]
  "T-02": 22
  "§4.1.1#r4": 23
  "§[F-FAAC-02] Edit Asset Class#p2": 25
  "ST-34": 26
  "FAAC-LOGIC-09d": 27
coverage:
  web: automated
---

# Apply Changes: Screening Dialog, Cancel, dan Apply dengan Effective From Bulan Berjalan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60, belum pernah diposting, tanpa versi Scheduled.
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini. Kemampuan membaca nilai tersimpan Useful Life dan Last Posted Period lewat fixture BE disediakan tim FE/BE.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Useful Life `B-ASSETS` kembali 60 (TC-308 menyimpan 48).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-ASSETS`, tekan Enter
2. Klik link Class Code `B-ASSETS` di tabel
3. Catat nilai Last Posted Period pada Detail sebagai baseline
4. Klik tab `Depreciation`
5. Ubah Useful Life dari 60 menjadi 48
6. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
7. Klik `Save`

### TC-FA-FAAC-307: Screening dialog Apply Changes saat Depreciation berubah pada Asset Class yang dipakai aset

8. Verifikasi Dialog `Apply Changes` tampil dengan Effective From (placeholder `Select month`) bernilai awal bulan berjalan (M)
9. Verifikasi checkbox `Apply to existing assets` tercentang dengan helper `Active assets follow the change from Effective From. Turn off to apply to new assets only.`
10. Verifikasi blok pratinjau `Assets affected` menampilkan 5
11. Verifikasi tombol `Cancel` dan `Apply` tampil
12. Verifikasi belum ada data tersimpan (Useful Life tersimpan masih 60, dibaca lewat fixture BE)

### TC-FA-FAAC-310: Cancel pada Apply Changes tidak menyimpan apa pun

13. Klik `Cancel` pada dialog
14. Verifikasi tidak ada toast yang tampil
15. Verifikasi dialog menutup
16. Verifikasi halaman Detail tetap terbuka dengan perubahan masih terisi (Useful Life 48)
17. Verifikasi tidak ada data tersimpan (Useful Life tersimpan tetap 60, dibaca lewat fixture BE)
18. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-308: Apply Changes dengan Effective From bulan berjalan

19. Klik `Save`
20. Pertahankan Effective From bulan berjalan dan klik `Apply`
21. Verifikasi halaman kembali ke tabel Asset Class (tidak ada versi Scheduled sesudah Save)
22. Verifikasi toast sukses `Success, asset class has been updated.` tampil di tabel
23. Verifikasi Useful Life 48 tampil di tabel (Commercial `Straight Line · 4 yrs` pada baris `B-ASSETS`)
24. Buka Detail `B-ASSETS` lagi dan klik tab `Depreciation`
25. Verifikasi Useful Life 48 pada form Detail
26. Verifikasi tidak ada Alert versi Scheduled
27. Verifikasi Last Posted Period tidak berubah dari baseline
28. Klik breadcrumb `Asset Class`
29. Klik `(←)` pada kotak Search

## Notes

1. Satu sesi edit Detail `B-ASSETS` dipakai bersama untuk TC-307, TC-310, dan TC-308: langkah TC nomor 1 sampai 4 identik pada ketiganya dan dijalankan sekali di langkah 2 sampai 5 dan 7 (langkah 6 mencatat baseline Changelog TC-310 sebelum Save); Save kedua (langkah 19) adalah langkah Save TC-308 pada form yang masih terisi perubahan dari TC-310. Urutan: screening dialog, Cancel, lalu Apply yang menyimpan data di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 3 (baseline Last Posted Period untuk asersi tidak berubah), langkah 6 (baseline Changelog, S-12), langkah 28 (kembali ke tabel), dan langkah 29 (mengosongkan Search). Langkah 24 membuka Detail kembali karena Expected TC-308 meminta nilai pada form Detail yang dibuka kembali.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan 5 aset aktif; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini). Target Apply adalah baris seed milik spec ini yang dipulihkan fixture BE.
4. S-05 dan P-1: Expected "tanpa log" pada TC-310 diasersi di spec ini (langkah 18) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Temuan untuk QA: Expected TC-308 c ("Periode yang sudah diposting tidak dihitung ulang") tidak punya cara observasi di TC karena `B-ASSETS` belum pernah diposting; spec hanya mengasersi bagian "Last Posted Period tidak berubah". Expected TC-307 a menyebut Effective From dengan placeholder `Select month` sekaligus bernilai awal bulan berjalan; spec mengasersi nilai awal bulan berjalan.
