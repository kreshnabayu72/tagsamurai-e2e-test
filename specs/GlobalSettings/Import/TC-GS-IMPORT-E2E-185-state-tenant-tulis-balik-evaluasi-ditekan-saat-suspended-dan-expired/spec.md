---
id: TC-GS-IMPORT-E2E-185-state-tenant-tulis-balik-evaluasi-ditekan-saat-suspended-dan-expired
title: "State tenant: tulis-balik evaluasi ditekan saat Suspended dan Expired, draft tersimpan saat turun ke plan Free dan naik kembali, produk Access dicabut dari organisasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-526
  - TC-GS-IMPORT-554
  - TC-GS-IMPORT-575
  - TC-GS-IMPORT-818
coverage:
  web: automated
---

# State tenant: tulis-balik evaluasi ditekan saat Suspended dan Expired, draft tersimpan saat turun ke plan Free dan naik kembali, produk Access dicabut dari organisasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state tenant global (produk organisasi Client E, plan Client C, status Client Suspended dan Expired) lewat fixture Admin Console; lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama:
  - Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`: aktor pertama (TC-526).
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_TC_PASSWORD`: ganti akun eksplisit (TC-554).
  - Total Control Client Suspended (Agus Wijaya) `totalControl_automated_qaTeam9@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`: ganti akun eksplisit (TC-575).
  - Total Control Client Expired (Citra Maharani) `totalControl_automated_qaTeam11@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTEXP_TC_PASSWORD`: ganti akun eksplisit (TC-818).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk setiap akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya; akun pelaku perubahan state tenant tidak disebut TC sehingga disediakan tim FE):
  - Fixture Admin Console: mencabut dan memulihkan produk Fixed Asset organisasi Client E; menurunkan plan Client C ke Free dan menaikkannya kembali ke Growth; men-Suspend dan meng-Expire client dan memulihkannya.
  - Skrip fixture inspeksi data: membaca status tersimpan baris draft dan counter Errors tersimpan (TC-575, 818).
  - Skrip fixture penyiapan: draft D-62 Client E, draft D-18 Client C, Client Suspended (draft User Login 8 baris dengan opsi `Siang` dihapus dari Custom Field `Shift` lalu di-Suspend, mengikuti D-05), dan Client Expired (D-75).
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal sesuai Data Uji TC):
  - D-62 `user-login-ref.csv` (draft User Login 3 baris `pending` Client E): Row # 1 Division `Gudang` Position `Technician`; Row # 2 Division `Warehouse` Access `Global Settings;Fixed Asset`; Row # 3 Division `Marketing`; Access `Global Settings` pada Row # 1 dan 3.
  - D-18 draft Brand 12 baris `pending` Client C dari `brand-12.csv`, plan Growth.
  - Client Suspended: master data seperti Client A (Kontrak Fixture R4), draft User Login 8 baris `pending` (isi seperti D-05) dengan Shift `Siang` pada Row # 1 dan 2; opsi `Siang` dihapus dari Custom Field `Shift`, lalu client di-Suspend (TC-575).
  - D-75 Client Expired: draft User Login 8 baris `pending` dengan Shift `Siang` pada Row # 1 dan 2; opsi `Siang` sudah dihapus dari Custom Field `Shift` dan client di-Expire (TC-818).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan produk Fixed Asset Client E, kembalikan plan Client C ke Growth, kembalikan Client Suspended (status Suspended) dan Client Expired (status Expired) ke kondisi Pre-setup (Kontrak Fixture R2), hapus draft Client E dan Client C, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-526: Produk Access dicabut dari organisasi

1. Reset Client E ke tanpa draft dan seed draft User Login D-62 (3 baris `pending`) lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab User Login
3. Cabut produk Fixed Asset dari Client E lewat fixture Admin Console
4. Tekan F5 pada halaman Import
5. Verifikasi Row # 2 (Access `Global Settings;Fixed Asset`) berstatus `error`
6. Verifikasi Error Summary Callout memuat `Access must only contain the following values: Global Settings` dengan badge "1 row"
7. Verifikasi Row # 1 dan 3 (Access `Global Settings`) tetap `pending`
8. Verifikasi Staging Metric Cards Ready to Import 2
9. Verifikasi Staging Metric Cards Errors 1
10. Pulihkan produk Fixed Asset Client E lewat fixture Admin Console

### TC-GS-IMPORT-554: Draft tersimpan saat client turun ke plan Free dan naik kembali

11. Ganti akun: logout, lalu login sebagai Total Control Client C (Rudi Hartanto)
12. Seed draft Brand D-18 (12 baris `pending`, plan Growth) Client C lewat skrip fixture
13. Buka Global Settings > Import, pilih Sub-Tab Brand
14. Turunkan plan Client C ke Free lewat fixture Admin Console
15. Buka halaman Import
16. Verifikasi halaman Import Disabled total dengan chip "Upgrade"
17. Verifikasi draft tidak dapat diakses
18. Naikkan plan Client C ke Growth lewat fixture Admin Console
19. Muat ulang halaman Import > Brand
20. Verifikasi Staging Table menampilkan draft 12 baris `pending`
21. Verifikasi Staging Metric Cards Total Rows 12
22. Verifikasi Staging Metric Cards Ready to Import 12
23. Verifikasi Staging Metric Cards Errors 0
24. Verifikasi Staging Metric Cards Duplicates 0

### TC-GS-IMPORT-575: Tulis-balik evaluasi ulang ditekan saat entitas Suspended

25. Ganti akun: logout, lalu login sebagai Total Control Client Suspended (Agus Wijaya)
26. Buka Global Settings > Import, pilih Sub-Tab User Login
27. Verifikasi Row # 1 tampil berstatus `error` hanya sebagai hasil hitung read-only
28. Verifikasi Row # 2 tampil berstatus `error` hanya sebagai hasil hitung read-only
29. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
30. Verifikasi status tersimpan Row # 1 dan 2 masih `pending` (tulis-balik ditekan)

### TC-GS-IMPORT-818: Tulis-balik evaluasi ulang ditekan saat entitas Expired

31. Ganti akun: logout, lalu login sebagai Total Control Client Expired (Citra Maharani)
32. Buka Global Settings > Import, pilih Sub-Tab User Login
33. Verifikasi Row # 1 tampil berstatus `error` hanya sebagai hasil hitung read-only
34. Verifikasi Row # 2 tampil berstatus `error` hanya sebagai hasil hitung read-only
35. Verifikasi kartu Errors menampilkan 2
36. Baca status tersimpan Row # 1 dan 2 serta counter Errors tersimpan lewat skrip fixture inspeksi data
37. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
38. Verifikasi counter Errors tersimpan 0 (tulis-balik ditekan)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: state tenant (h); objek uji adalah perilaku Import saat produk organisasi dicabut, plan turun, serta status Suspended dan Expired. Fixture Admin Console adalah pemicu perubahan state tenant. Verifikasi baca per tier (bukan perubahan tier) untuk plan gating ada di spec 059.
- Alasan melewati sekitar 35 langkah (38 langkah nominal): empat blok homogen satu kelas state tenant yang berdiri sendiri dengan penyiapan dan pemulihan tenant di dalam blok. Urutan blok dikelompokkan per akun dengan langkah ganti akun eksplisit (langkah 11, 25, 31) sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 12), pembukaan halaman dan Sub-Tab, perubahan produk dan plan lewat fixture Admin Console (langkah 3, 10, 14, 18), muat ulang, pembacaan status tersimpan (langkah 29, 36), dan ganti akun. Langkah 17 (draft tidak dapat diakses) didahului langkah 16 (halaman Disabled dengan chip "Upgrade") sebagai pembuktian state.
- Temuan untuk QA:
  - TC-GS-IMPORT-575 Precondition c menyiapkan draft "isi seperti D-05" di Client Suspended lewat skrip fixture, sedangkan D-72 sampai D-74 tidak mencakup draft User Login 8 baris untuk Suspended; ketergantungan hanya pada precondition TC (tidak ada entri Data Dinamis).
  - TC-GS-IMPORT-526 dikelompokkan pada kelas state tenant (keputusan penyusun rencana); sebagai alternatif ia dapat menjadi spec fungsional karena objek uji adalah evaluasi ulang Access, bukan lockdown tenant.
  - TC-GS-IMPORT-554 Expected a menyebut halaman Import "Disabled total" dengan chip "Upgrade" tanpa menyebut elemen yang diasersi (toolbar, tombol, atau seluruh halaman); spec mengasersi halaman sebagaimana kata TC.
  - Post Condition TC-GS-IMPORT-526, 554, 575, 818 (fixture dipulihkan; plan kembali Growth; Client Suspended dan Expired dipulihkan) dikerjakan langkah 10, 18, dan hook `after`; tidak diasersi (S-01).
