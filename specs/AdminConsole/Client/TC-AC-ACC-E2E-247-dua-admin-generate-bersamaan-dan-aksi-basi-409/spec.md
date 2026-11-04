---
id: TC-AC-ACC-E2E-247-dua-admin-generate-bersamaan-dan-aksi-basi-409
title: "Dua Admin: Generate Enrollment QR Bersamaan, Deactivate Station Basi, dan Revoke Tablet Basi (409)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-320
  - TC-AC-ACC-974
  - TC-AC-ACC-975
coverage:
  web: automated
---

# Dua Admin: Generate Enrollment QR Bersamaan, Deactivate Station Basi, dan Revoke Tablet Basi (409)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script) untuk Sesi A. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Sesi B: akun Active-Full kedua yang disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_B_PASSWORD` (nama env baru, didaftarkan pada tahap script).
- Kemampuan teknis (kelas harness c, konteks kedua menjadi objek asersi): dua konteks browser terpisah (Sesi A dan Sesi B) yang masing-masing login lewat UI; sinkronisasi klik bersamaan antar-sesi (TC-AC-ACC-320); baca status token Enrollment QR lewat fixture BE (disediakan tim FE/BE). Konteks Sesi B ditutup dan sesi login browser terkait dihapus di akhir tiap TC (S-09).
- Data Dinamis milik spec (skrip seed, bukan lewat UI; dihapus di hook `after`): Client "PT Race QR {runId}-247" (Active, FAMS Active; Asset Control Total 3 / Used 0 / Available 3; satu SFR bertipe Asset Control "Reader Race" tanpa station aktif; tanpa token Active) untuk TC-AC-ACC-320 (TC memakai "PT Sejahtera Abadi" Pre-setup yang dihindari agar token Active tidak tertinggal di Client bersama).
- Data Dinamis milik spec (kembaran fixture; skrip seed di hook `before`, bukan lewat UI; dihapus di hook `after`; Deactivate dan Revoke permanen sehingga spec tidak memakai C-FX10-1 dan C-FX10-2 bersama [S-06]; Company Name bersuffix `{runId}-247`, atribut setara baris fixture asal di Tabel A3 (Partner CV Mitra Sejati; Group Area Jakarta; FAMS Active), nama SFR, Station, dan Tablet di dalam kembaran sama dengan fixture asal karena terlingkup pada Client kembaran):
  - "PT Uji Basi Deactivate {runId}-247" (kembaran C-FX10-1, TC-AC-ACC-974): Asset Control Total 4 / Used 2 / Available 2; Station "Stasiun Basi Deactivate" Active dengan Tablet "Tablet Basi Deactivate 1" Active, dan Station "Stasiun Basi Pendamping" Active dengan Tablet "Tablet Basi Pendamping 1" Active; setiap Station dibuat dari token Enrollment Used; tanpa token Active.
  - "PT Uji Basi Revoke {runId}-247" (kembaran C-FX10-2, TC-AC-ACC-975): Total 3 / Used 1 / Available 2; Station "Stasiun Basi Revoke" Active dengan Tablet "Tablet Basi Revoke 1" dan "Tablet Basi Revoke 2" Active, dibuat dari token Enrollment Used; tanpa token Active.
- Kemampuan teknis tambahan: jam server uji dapat dimajukan (token Active hasil TC-AC-ACC-320 dikembalikan ke Expired dengan memajukan jam server 15 menit di langkah penghubung 8 dan di hook `after`; jam dipulihkan); baca jumlah baris Changelog Asset Control lewat Search di modal (baseline, S-12).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- State global: jam server dimajukan lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` dan `AC_CLIENT_ACTIVE_FULL_B_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-320: Dua admin generate bersamaan: token lama di-invalidate

1. [Sesi A] Ketik Search "PT Race QR {runId}-247" di List Client, tekan Enter, klik Company Name hasilnya, lalu klik Tab Asset Control
2. [Sesi B] Login sebagai akun Active-Full kedua, ketik Search "PT Race QR {runId}-247", tekan Enter, klik Company Name hasilnya, lalu klik Tab Asset Control
3. [Sesi A dan Sesi B] Klik [Generate Enrollment QR] bersamaan
4. [Sesi A dan Sesi B] Tunggu aksi selesai (dialog "Enrollment QR" atau dialog "Active Enrollment QR" tampil di masing-masing sesi)
5. Verifikasi hanya satu token Enrollment QR berstatus `Active` untuk Client (dibaca lewat fixture BE)
6. Verifikasi token lain berstatus `Invalidated` (dibaca lewat fixture BE)
7. [Sesi A dan Sesi B] Tutup dialog yang tampil, lalu tutup konteks Sesi B dan hapus sesi login browsernya
8. Majukan jam server uji 15 menit hingga token Active menjadi Expired, lalu pulihkan jam server dan jam browser

### TC-AC-ACC-974: Deactivate Station dari UI basi: 409, dialog konflik, list di-refresh

9. [Sesi A] Klik breadcrumb "Client", klik sub-tab Active, ketik Search "PT Uji Basi Deactivate {runId}-247", tekan Enter, klik Company Name "PT Uji Basi Deactivate {runId}-247", klik Tab Asset Control, dan catat Station Quota serta Status "Stasiun Basi Deactivate"
10. Verifikasi (Sesi A) Status "Stasiun Basi Deactivate" `Active` dan Station Quota Total 4, Used 2, Available 2
11. [Sesi A] Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Stasiun Basi Deactivate", tekan Enter, catat jumlah baris (L0), lalu tutup modal
12. [Sesi A] Buka ⋯ Station "Stasiun Basi Deactivate" lalu klik Deactivate (dialog tetap terbuka)
13. Verifikasi (Sesi A) dialog Title "Deactivate Station" dengan bullet `• Stasiun Basi Deactivate`
14. [Sesi B] Login sebagai akun Active-Full kedua, klik sub-tab Active, ketik Search "PT Uji Basi Deactivate {runId}-247", tekan Enter, klik Company Name hasilnya, klik Tab Asset Control, buka ⋯ Station "Stasiun Basi Deactivate", klik Deactivate, lalu klik [Deactivate] pada dialog
15. Verifikasi (Sesi B) toast sukses: "Success, station has been deactivated."
16. [Sesi A] Klik [Deactivate] pada dialog yang masih terbuka
17. Verifikasi (Sesi A) dialog konflik tampil tanpa Title, hanya berisi teks "This station was changed by someone else. Please review." dan tombol [OK]
18. Verifikasi (Sesi A) toast "Success, station has been deactivated." tidak tampil
19. [Sesi A] Klik [OK] pada dialog konflik
20. Verifikasi (Sesi A) dialog konflik tertutup
21. Verifikasi (Sesi A) Status "Stasiun Basi Deactivate" berbadge `Deactivated` (danger) dan kolom Tablets 0
22. Verifikasi (Sesi A) Station Quota: Total 4, Used 1, Available 3 (hanya berkurang satu oleh Sesi B, bukan Used 0)
23. [Sesi A] Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Stasiun Basi Deactivate", tekan Enter, lalu hitung baris (L1)
24. Verifikasi L1 = L0 + 1
25. Verifikasi baris baru: Action `Deactivate Station`, Object `Stasiun Basi Deactivate`, Field `Status`, Old Value `Active`, New Value `Deactivated` (request basi tidak menambah baris)
26. Tutup modal Changelog, lalu tutup konteks Sesi B dan hapus sesi login browsernya

### TC-AC-ACC-975: Revoke Tablet dari UI basi: 409, dialog konflik, list di-refresh

27. [Sesi A] Klik breadcrumb "Client", klik sub-tab Active, ketik Search "PT Uji Basi Revoke {runId}-247", tekan Enter, klik Company Name "PT Uji Basi Revoke {runId}-247", klik Tab Asset Control, dan catat Station Quota serta kolom Tablets "Stasiun Basi Revoke"
28. Verifikasi (Sesi A) kolom Tablets "Stasiun Basi Revoke" = 2 dan Station Quota Total 3, Used 1, Available 2
29. [Sesi A] Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Tablet Basi Revoke 1", tekan Enter, catat jumlah baris (L2), lalu tutup modal
30. [Sesi A] Klik row Station "Stasiun Basi Revoke" untuk expand Tablet List, buka ⋯ Tablet "Tablet Basi Revoke 1" lalu klik Revoke (dialog tetap terbuka)
31. Verifikasi (Sesi A) dialog Title "Revoke Tablet" dengan bullet `• Tablet Basi Revoke 1`
32. [Sesi B] Login sebagai akun Active-Full kedua, klik sub-tab Active, ketik Search "PT Uji Basi Revoke {runId}-247", tekan Enter, klik Company Name hasilnya, klik Tab Asset Control, klik row Station "Stasiun Basi Revoke" untuk expand Tablet List, buka ⋯ Tablet "Tablet Basi Revoke 1", klik Revoke, lalu klik [Revoke] pada dialog
33. Verifikasi (Sesi B) toast sukses: "Success, tablet has been revoked."
34. [Sesi A] Klik [Revoke] pada dialog yang masih terbuka
35. Verifikasi (Sesi A) dialog konflik tampil tanpa Title, hanya berisi teks "This tablet was changed by someone else. Please review." dan tombol [OK]
36. Verifikasi (Sesi A) toast "Success, tablet has been revoked." tidak tampil
37. [Sesi A] Klik [OK] pada dialog konflik
38. Verifikasi (Sesi A) dialog konflik tertutup
39. Verifikasi (Sesi A) kolom Tablets "Stasiun Basi Revoke" = 1 (Revoked tidak dihitung)
40. Verifikasi (Sesi A) Status Station "Stasiun Basi Revoke" `Active`
41. Verifikasi (Sesi A) Station Quota Total 3, Used 1, Available 2 (tidak berubah)
42. [Sesi A] Klik ikon Changelog di Tab Asset Control, ubah ukuran halaman modal menjadi 100 baris, ketik Search "Tablet Basi Revoke 1", tekan Enter, lalu hitung baris (L3)
43. Verifikasi L3 = L2 + 1
44. Verifikasi baris baru: Action `Revoke Tablet`, Object `Tablet Basi Revoke 1`, Field `Status`, Old Value `Active`, New Value `Revoked` (request basi tidak menambah baris)
45. Tutup modal Changelog, lalu tutup konteks Sesi B dan hapus sesi login browsernya

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 2, 9, 14, 27, 32 (Search dan buka Detail Client serta login Sesi B; hook suite hanya membuka List Client), langkah 7, 26, 45 (menutup dialog, modal, dan konteks Sesi B, S-09), langkah 8 (memulihkan token Active menjadi Expired; TC-AC-ACC-320 tidak menulis Post Condition), langkah 30 (expand row).
- Baseline (S-12): langkah 11 dan 29 mencatat jumlah baris Changelog sebelum aksi (L0, L2) sesuai TC; Search di modal dan ukuran halaman 100 agar baris yang dihitung berada di halaman teramati (S-14).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (c, dua sesi browser pada Client yang sama atau terpisah) dan tiap blok berdiri sendiri (Client berbeda; konteks Sesi B ditutup di akhir blok).
- Replika S-06 [KEPUTUSAN 2026-11-03]: Deactivate dan Revoke bersifat permanen, sehingga TC-AC-ACC-974 dan 975 memakai kembaran C-FX10-1 dan C-FX10-2 bersuffix `{runId}-247` pada Group Area Jakarta (seed di `before`, cleanup di `after`); Sesi A dan Sesi B tetap Active-Full yang menjangkau Area Jakarta.
- Temuan untuk QA:
  - TC-AC-ACC-320 menyebut "Admin A dan B klik Generate bersamaan" pada "PT Sejahtera Abadi" tanpa mekanisme sinkronisasi klik dan tanpa observasi status token di UI; spec memakai Client sendiri, kemampuan klik bersamaan, dan pembacaan status token lewat fixture BE.
  - TC-AC-ACC-974 dan TC-AC-ACC-975 menyebut "Sesi A dan Sesi B" dengan role Active-Full yang sama tanpa menyebut akunnya; bila akun sama, batas sesi web per akun dapat mengusir Sesi A, sehingga spec memerlukan akun kedua yang disediakan tim FE.
