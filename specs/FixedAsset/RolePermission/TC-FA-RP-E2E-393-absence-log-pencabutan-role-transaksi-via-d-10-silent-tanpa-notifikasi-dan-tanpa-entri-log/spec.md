---
id: TC-FA-RP-E2E-393-absence-log-pencabutan-role-transaksi-via-d-10-silent-tanpa-notifikasi-dan-tanpa-entri-log
title: "Absence log: pencabutan Role Transaksi lewat D-10 bersifat silent, tanpa notifikasi dan tanpa entri log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1233
coverage:
  web: automated
---

# Absence log: pencabutan Role Transaksi lewat D-10 bersifat silent, tanpa notifikasi dan tanpa entri log

## Prerequisites

- Mode: FE+BE.
- Akun:

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Manage global user & role dengan Update, Hendra Wijaya | #6 | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| 2 (langkah 29) | Gunawan Halim (penerima notifikasi) | #17 | tidak tertulis di Pre-setup #17; akun disediakan tim FE | `Spectra.env.FA_GUNAWAN_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group: `Helpdesk`, `Data Center`), dan #19 (baris pola Asset Admin pada `Helpdesk` sub-tab `Disposal`; menjadi baris pembanding langkah 14).
- Seeding precondition (hook `before`, dipakai sebagai precondition TC, tidak diasersi; kemampuan seeding disediakan tim FE/BE, tanpa endpoint karangan): Gunawan Halim (Pre-setup #17) diatur tanpa Home Group, lalu ditugaskan Asset Admin pada `Helpdesk` sub-tab `Disposal`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri Changelog Transaction Role sub-tab `Disposal`, System Log Hendra Wijaya, dan Activity Log FAMS sebagai baseline (audit trail permanen, S-12 dan bagian 8b butir 10); membaca jumlah notifikasi in-app Gunawan Halim sebagai baseline (bagian 8b butir 10). Jendela absence notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" (pilihan spec, bukan nilai TC atau PRD; langkah 32). Seluruh baseline dicatat tepat sebelum pemicu (langkah 1 sampai 4).
- State yang diubah dan pemulihannya: Home Group Gunawan Halim menjadi `Data Center` dan baris Asset Admin `Helpdesk` Gunawan Halim tercabut (itu aksi yang diuji). Hook `after` (tidak berasumsi langkah spec berhasil penuh) mencabut baris seed bila masih ada dan memulihkan Home Group Gunawan Halim ke `Data Center` (Pre-setup #17), lewat fixture BE. Entri log bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`, `FA_GUNAWAN_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1233: Pencabutan Role Transaksi akibat constraint baru silent: tanpa notifikasi dan tanpa entri log

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Transaction Role sub-tab `Disposal`
2. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri System Log Hendra Wijaya
3. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri Activity Log FAMS
4. Catat baseline (aksi tanpa `Verifikasi`): jumlah notifikasi in-app Gunawan Halim
5. Buka Settings > User lewat sidebar
6. Ketik Search `Gunawan Halim`, tekan Enter
7. Klik Name `Gunawan Halim`
8. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
9. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`
10. Klik `[Revoke]`
11. Verifikasi Home Group Gunawan Halim tersimpan `Data Center`
12. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Transaction Role`
13. Klik node `Helpdesk` lalu klik sub-tab `Disposal`
14. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin `Helpdesk`
15. Verifikasi Gunawan Halim tidak lagi tampil di section Asset Admin `Helpdesk`
16. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
17. Verifikasi modal Changelog sub-tab `Disposal` tampil dengan jumlah entri yang terbaca
18. Verifikasi entri baru sejak baseline langkah 1 tidak memuat entri `Remove`, `Remove (via ...)`, maupun `Auto-Revert` untuk Field `Asset Admin — Helpdesk` dengan Old Value `Gunawan Halim`
19. Tutup modal Changelog
20. Buka Settings > User lewat sidebar
21. Ketik Search `Hendra Wijaya`, tekan Enter
22. Klik Name `Hendra Wijaya`
23. Klik Tab `System Log`
24. Verifikasi System Log tampil dengan jumlah entri yang terbaca
25. Verifikasi entri baru sejak baseline langkah 2 tidak memuat entri pencabutan penugasan Asset Admin `Helpdesk` milik Gunawan Halim
26. Buka Activity Log FAMS (menu Activity Log)
27. Verifikasi Activity Log tampil dengan jumlah entri yang terbaca
28. Verifikasi entri baru sejak baseline langkah 3 tidak memuat entri pencabutan penugasan Asset Admin `Helpdesk` milik Gunawan Halim
29. Ganti akun: logout, lalu login sebagai Gunawan Halim dengan `Spectra.env.FA_GUNAWAN_PASSWORD`
30. Buka Overlay Notifikasi lewat Bell icon navbar
31. Verifikasi Overlay Notifikasi tampil
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi jumlah notifikasi Gunawan Halim sama dengan baseline langkah 4 (tidak ada notifikasi tentang pencabutan penugasan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah.
- Kelas g (absence log) dengan pemicu multi-konteks (ganti akun ke Gunawan Halim pada langkah 29 untuk mengamati notifikasi). Pemicu (D-10 `[Revoke]`) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji lain (`P-5` butir a). Klausa a TC (baris Gunawan Halim hilang, langkah 15) berada di spec yang sama karena bergantung pada state hasil `[Revoke]` yang sama dan berfungsi sebagai anchor positif (`P-1`, S-05). Perilaku fungsional D-10 (dialog dan pencabutan Group Role dan Group Manager) diasersi di spec 392 dan spec D-10 lain; TC-FA-RP-1233 hanya ada di spec ini.
- Anchor positif absence (bagian 8b butir 2): `[Revoke]` yang diproses terbukti dari Home Group tersimpan `Data Center` (langkah 11), baris Gunawan Halim hilang di tabel yang tetap memuat baris pembanding (langkah 14 dan 15), tiap surface log tampil dengan jumlah entri yang terbaca (langkah 17, 24, 27), dan Overlay Notifikasi tampil (langkah 31) dengan jendela 5 detik (langkah 32; bagian 6 dan 8b butir 11) sebelum asersi absence notifikasi (langkah 33). Notifikasi dibandingkan sebagai jumlah total terhadap baseline per penerima (bagian 8b butir 10).
- Cara baca entri baru (S-14): entri baru sejak baseline dibaca pada baris teratas urutan default `Date` terbaru sebanyak selisih jumlah entri terhadap baseline; bila selisih nol, asersi absence lulus dengan anchor di atas. Asersi tidak memakai total absolut dan tidak mengandalkan urutan antar entri yang jatuh pada menit yang sama.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 sampai 4 (baseline, S-12); langkah 5 sampai 7 dan 20 sampai 22 (membuka Detail User; Search pada langkah 6 dan 21 menemukan baris target, R-16); langkah 10 (`[Revoke]` adalah langkah TC); langkah 12, 13, 16, 19, 23, 26, 30 (navigasi, membuka dan menutup modal); langkah 29 (ganti akun, S-07; layar yang dibutuhkan dibuka eksplisit pada langkah 30); langkah 32 (jendela absence notifikasi). Verifikasi langkah 9, 11, 14, 17, 24, 27, 31 adalah anchor positif yang tidak ada di Expected TC (S-03): bukti `[Revoke]` diproses dan surface termuat.
- Asersi longgar pada langkah 18, 25, dan 28 sengaja tidak menyebut bentuk Field penugasan di System Log dan Activity Log, dan pada Changelog memakai kecocokan Field `Asset Admin — Helpdesk` sebagaimana TC; baseline membatasi pembacaan pada entri baru supaya entri lama dari spec lain tidak memengaruhi hasil.
- Temuan untuk QA:
  - NC-20 (PRD Open Item #9) menunggu PM: pencabutan silent Role Transaksi (tanpa notifikasi dan tanpa entri log) adalah bagian arah gate yang belum dikonfirmasi; bila PM memutuskan pencabutan dicatat, seluruh asersi absence spec ini berbalik.
  - TC-FA-RP-1233 langkah 2 menyebut `Auto-Revert`, tetapi TC tidak menulis bentuk Field penugasan di Changelog selain `Asset Admin — Helpdesk` dengan Old Value `Gunawan Halim`; spec memakai teks itu dan tidak mengarang Old Value, New Value, atau Modified By entri.
  - TC-FA-RP-1233 langkah 3 menyebut "Detail aktor" tanpa menyebut akunnya; spec memakai Hendra Wijaya (aktor pengedit Home Group, Pre-setup #6) dan membuka System Log lewat Detail User serta Activity Log FAMS lewat menu Activity Log.
  - Penetapan Home Group sendiri dapat menulis entri Activity Log atau System Log aktor dan notifikasi; TC tidak menyebutnya. Spec hanya mengasersi bahwa tidak ada entri pencabutan penugasan itu dan bahwa jumlah notifikasi Gunawan Halim sama dengan baseline; bila penetapan Home Group menghasilkan notifikasi, asersi langkah 33 gagal dan TC perlu merinci jenis notifikasi yang dimaksud.
  - Email akun Gunawan Halim tidak tertulis di Pre-setup #17; akun disediakan tim FE. Nama env `FA_GUNAWAN_PASSWORD` sudah terdaftar di `suite.md`.
  - Precondition TC menyebut Gunawan Halim "tanpa Home Group" sedangkan Pre-setup #17 menyatakan Home Group `Data Center`; spec mengaturnya lewat seeding hook `before` dan memulihkannya di hook `after`.
  - Post Condition TC-FA-RP-1233 kosong ("-").
