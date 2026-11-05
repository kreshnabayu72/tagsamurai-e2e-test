---
id: TC-GS-IMPORT-E2E-153-kontrol-worker-commit-accept-ai-dan-create-missing-divisions-positions
title: "Kontrol worker commit: Accept AI dan Create Missing (Divisions, Positions) Disabled dengan tooltip selama committing"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-306
  - TC-GS-IMPORT-339
  - TC-GS-IMPORT-728
  - TC-GS-IMPORT-745
coverage:
  web: automated
---

# Kontrol worker commit: Accept AI dan Create Missing (Divisions, Positions) Disabled dengan tooltip selama committing

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit, mode mock AI) dan memakai Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - Kontrol worker commit D-47 mode 1 (dijeda sebelum job mulai, sehingga job yang dimulai tetap `committing`) untuk TC-306, 339, 728, dan mode 2 (dijeda di dalam batch pertama sesudah uji ulang late-binding) untuk TC-745.
  - Mock layanan AI deterministik mode normal D-40 (tabel D-41 dan D-42: `Gudng` menghasilkan saran `Gudang` 0,91).
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus hasil commit) dan seeding draft TC-745.
- Data Pre-setup Client E (hanya dibaca, tidak diubah spec ini): Division 5 item (`Logistik` belum ada) dan Position 5 item (`Store Supervisor` belum ada); Division `Gudang` ada.
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal; tidak ada record master data tercipta karena worker dijeda):
  - D-44 `brand-ai-commit.csv`: kolom `Brand Name`; `Lenovo`, `Dell`, nilai sumber Brand D-41 (121 karakter, badge saran `Samsung Electronics Indonesia`).
  - D-45 `user-login-commit-logistik.csv`: baris #1 Bambang Hartono Division `Engineering`; baris #2 Citra Wulandari dan #3 Doni Kurniawan Division `Logistik`; Position kosong.
  - D-45 `user-login-commit-store-supervisor.csv`: baris #1 Bambang Hartono Division `Engineering` Position kosong; baris #2 Citra Wulandari dan #3 Doni Kurniawan Division `Engineering` Position `Store Supervisor`.
  - `user-login-gudng-3.csv` (draft seed TC-745): #1 Vina Lestari `vina.lestari@example.com` Division `Gudng` Access `Global Settings` (`error`); #2 Wawan Setiawan `wawan.setiawan@example.com` Division `Engineering`; #3 Xena Pratiwi `xena.pratiwi@example.com` Division `Engineering`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, kembalikan mock AI ke normal, hapus draft Client E, hapus hasil commit bila ada, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-306: Accept dan Dismiss Disabled selama committing

1. Reset Client E (D-47) ke tanpa draft; pastikan mock AI mode normal
2. Muat ulang halaman Import > Brand
3. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
4. Klik `[Upload File]` di Dropzone dan pilih berkas `brand-ai-commit.csv`
5. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
6. Klik `[Import (2)]`
7. Verifikasi footer `[Import (2)]` tampil Disabled
8. Arahkan kursor ke `[Accept]` pada badge saran sel Brand Name baris #3
9. Verifikasi `[Accept]` tetap tampil dan Disabled
10. Verifikasi tooltip pada `[Accept]` "Can't do this while an import is in progress."
11. Arahkan kursor ke `[Dismiss]` pada badge saran sel Brand Name baris #3
12. Verifikasi `[Dismiss]` tetap tampil dan Disabled
13. Verifikasi tooltip pada `[Dismiss]` "Can't do this while an import is in progress."

### TC-GS-IMPORT-339: Create Missing Divisions per-baris dan bulk Disabled selama committing

14. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit
15. Pilih Sub-Tab User Login
16. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
17. Klik `[Upload File]` di Dropzone dan pilih berkas `user-login-commit-logistik.csv`
18. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
19. Klik `[Import (1)]`
20. Verifikasi footer `[Import (1)]` tampil Disabled
21. Klik `⋯` pada baris #2
22. Arahkan kursor ke `[Create Missing Divisions]` pada menu `⋯`
23. Verifikasi `[Create Missing Divisions]` pada menu `⋯` baris #2 tampil Disabled
24. Verifikasi tooltip pada `[Create Missing Divisions]` menu `⋯` "Can't do this while an import is in progress."
25. Tutup menu `⋯`
26. Arahkan kursor ke `[Create Missing Divisions]` pada Error Summary Callout
27. Verifikasi `[Create Missing Divisions]` pada Error Summary Callout tampil Disabled
28. Verifikasi tooltip pada `[Create Missing Divisions]` Error Summary Callout "Can't do this while an import is in progress."

### TC-GS-IMPORT-728: Create Missing Positions per-baris dan bulk Disabled selama committing

29. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit
30. Muat ulang halaman Import > User Login
31. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
32. Klik `[Upload File]` di Dropzone dan pilih berkas `user-login-commit-store-supervisor.csv`
33. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
34. Klik `[Import (1)]`
35. Verifikasi footer `[Import (1)]` tampil Disabled
36. Klik `⋯` pada baris #2
37. Arahkan kursor ke `[Create Missing Positions]` pada menu `⋯`
38. Verifikasi `[Create Missing Positions]` pada menu `⋯` baris #2 tampil Disabled
39. Verifikasi tooltip pada `[Create Missing Positions]` menu `⋯` "Can't do this while an import is in progress."
40. Tutup menu `⋯`
41. Arahkan kursor ke `[Create Missing Positions]` pada Error Summary Callout
42. Verifikasi `[Create Missing Positions]` pada Error Summary Callout tampil Disabled
43. Verifikasi tooltip pada `[Create Missing Positions]` Error Summary Callout "Can't do this while an import is in progress."

### TC-GS-IMPORT-745: Accept dan Create Missing Divisions pada Tab User Login Disabled dengan tooltip

44. Reset Client E (D-47) ke tanpa draft dan pulihkan worker commit; seed draft User Login `user-login-gudng-3.csv` (2 `pending`, baris #1 `error` dengan Division `Gudng`) lewat skrip fixture; pastikan mock AI mode normal
45. Muat ulang halaman Import > User Login
46. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
47. Klik `[Import (2)]`
48. Tunggu aksi selesai (permintaan mendapat respons)
49. Muat ulang halaman Import > User Login
50. Hover `[Accept]` pada badge saran Division baris #1
51. Verifikasi `[Accept]` pada badge saran tetap tampil dan Disabled
52. Verifikasi tooltip pada `[Accept]` "Can't do this while an import is in progress."
53. Hover `[Create Missing Divisions]` pada Error Summary Callout
54. Verifikasi `[Create Missing Divisions]` pada Error Summary Callout tetap tampil dan Disabled
55. Verifikasi tooltip pada `[Create Missing Divisions]` Error Summary Callout "Can't do this while an import is in progress."
56. Buka menu `⋯` baris #1
57. Hover `[Create Missing Divisions]` pada menu
58. Verifikasi `[Create Missing Divisions]` pada menu `⋯` baris #1 tetap tampil dan Disabled
59. Verifikasi tooltip pada `[Create Missing Divisions]` menu `⋯` "Can't do this while an import is in progress."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah state `committing` yang dibentuk kontrol worker D-47. Mock AI normal hanya pemicu badge saran (P-2).
- Alasan melewati sekitar 35 langkah (59 langkah nominal): empat blok homogen (tombol Disabled dengan tooltip selama `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 14, 29, 44), aktivasi kontrol worker (langkah 3, 16, 31, 46), pembukaan halaman dan Sub-Tab, "Muat ulang halaman Import > <Sub-Tab>" sesudah reset (langkah 2, 30, 45; reset membuang atau mengganti draft sementara halaman Import dari blok atau hook sebelumnya masih terbuka, `suite.md`), menutup menu `⋯` (langkah 25, 40), langkah 48 (Tunggu aksi selesai: permintaan mendapat respons, memisahkan klik `[Import (2)]` dari muat ulang), dan muat ulang (langkah 49). Tooltip diasersi sebelum langkah berikutnya yang mengubah state hover (butir 5 bagian 8b).
- Penanda selesai untuk langkah 48 tidak disebut di TC atau PRD; "permintaan mendapat respons" dipakai sampai QA menetapkan penanda yang teramati.
- Pembagian TC lintas spec: TC-GS-IMPORT-745 dan TC-GS-IMPORT-918 (Create Missing Options saat `committing`) berpola sama; TC-GS-IMPORT-918 ada di spec 145.
- Temuan untuk QA:
  - TC-GS-IMPORT-306, 339, 728, 745 tidak merujuk kontrol worker D-47 pada kolom D-ref walau butuh worker dijeda; TC-GS-IMPORT-306, 339, 728 menyebut D-47 hanya di Precondition e.
  - TC-GS-IMPORT-745 menyebut draft disiapkan oleh Precondition c tanpa langkah upload, dan menyebut berkas `user-login-gudng-3.csv` pada Data Uji; spec men-seed draft lewat fixture dan tidak mengunggah berkas.
  - Post Condition TC-GS-IMPORT-306, 339, 728, 745 (worker dilanjutkan dan Client E dipulihkan, atau "job committing dengan worker dijeda") tidak punya langkah observasi dan tidak diasersi (S-01); pemulihan dikerjakan hook `after`.
  - Pola identik (Create Missing saat `committing`) juga ada di TC-GS-IMPORT-729 dan 730 sebagai request langsung (spec 145); TC-GS-IMPORT-339 dan 728 hanya mengasersi UI.
  - TC-GS-IMPORT-745 Expected a menyebut `[Accept]` pada badge saran Division baris #1 tampil walau baris #1 `error` pada job `committing`; baris `error` bukan anggota batch aktif, tetapi tombol tetap Disabled menurut Expected. Tidak ada rujukan PRD pada kolom TC yang menjelaskan alasannya selain §4.3 Committing.
