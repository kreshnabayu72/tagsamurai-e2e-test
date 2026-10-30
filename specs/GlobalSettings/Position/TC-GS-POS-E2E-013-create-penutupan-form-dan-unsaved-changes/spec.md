---
id: TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes
title: "Create Position: Penutupan Form via ✕ dan Esc, Dialog Unsaved Changes (Cancel dan Leave), Backdrop, Reload, dan Pindah Menu"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-55
  - TC-GS-POS-56
  - TC-GS-POS-57
  - TC-GS-POS-58
  - TC-GS-POS-59
  - TC-GS-POS-60
  - TC-GS-POS-61
  - TC-GS-POS-62
  - TC-GS-POS-63
  - TC-GS-POS-64
coverage:
  web: automated
---

# Create Position: Penutupan Form via ✕ dan Esc, Dialog Unsaved Changes (Cancel dan Leave), Backdrop, Reload, dan Pindah Menu

## Prerequisites

- Mode: FE+BE (backend nyata).
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`; langkah 1 langsung membuka popup Create.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: tidak ada record yang dibuat. Nama `Risk Analyst {runId}-013` hanya diketik dan tidak pernah disimpan (setiap kasus berakhir dengan penutupan form tanpa Submit). Fixture baru `Fixture.position.createClose013`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API Position `Risk Analyst {runId}-013` bila ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: penekanan Esc; klik pada area backdrop di luar popup; muat ulang halaman (F5) dengan penanganan dialog `beforeunload` browser (mendeteksi kemunculannya dan menolaknya agar tetap di halaman), serta pemuatan ulang tanpa dialog saat form bersih; klik menu sidebar Global Settings > General Settings.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-POS-55: Tutup via ✕ saat form bersih

1. Klik `[+ Position]`
2. Klik `[✕]` tanpa mengisi apa pun
3. Verifikasi popup langsung tertutup
4. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-56: Tutup via Esc saat form bersih

5. Klik `[+ Position]`
6. Tekan Esc tanpa mengisi apa pun
7. Verifikasi popup langsung tertutup
8. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-57: Tutup via ✕ saat form terisi memunculkan Dialog Unsaved Changes

9. Klik `[+ Position]`
10. Ketik `Risk Analyst {runId}-013` pada Position Name
11. Klik `[✕]`
12. Verifikasi Header dialog menampilkan Title "Unsaved Changes"
13. Verifikasi Title dialog ber-severity warning
14. Verifikasi Body dialog menampilkan "You have unsaved changes. Are you sure you want to leave?"
15. Verifikasi Footer dialog menampilkan `[Cancel]` bergaya text (contrast)
16. Verifikasi Footer dialog menampilkan `[Leave]` bergaya filled (warning)
17. Verifikasi Popup Create masih terlihat di belakang dialog

### TC-GS-POS-58: Cancel pada Dialog Unsaved Changes

18. Klik `[Cancel]`
19. Verifikasi dialog tertutup
20. Verifikasi Popup Create tetap terbuka
21. Verifikasi Position Name tetap berisi `Risk Analyst {runId}-013`

### TC-GS-POS-59: Leave pada Dialog Unsaved Changes

22. Klik `[✕]`
23. Verifikasi dialog Unsaved Changes tampil
24. Klik `[Leave]`
25. Verifikasi dialog tertutup
26. Verifikasi popup tertutup
27. Verifikasi tidak ada toast
28. Ketik Search `Risk Analyst {runId}-013`, tekan Enter
29. Verifikasi area tabel menampilkan Title "No results found"
30. Verifikasi `Risk Analyst {runId}-013` tidak muncul di tabel
31. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

### TC-GS-POS-63: Reload tab saat form bersih tanpa konfirmasi browser

32. Klik `[+ Position]`
33. Tekan F5 tanpa mengisi apa pun
34. Verifikasi tidak ada dialog `beforeunload` browser yang muncul
35. Verifikasi tabel Position tampil
36. Verifikasi halaman ter-reload: Popup Create tidak lagi tampil

### TC-GS-POS-60: Esc saat form terisi memunculkan Dialog Unsaved Changes

37. Klik `[+ Position]`
38. Ketik `Risk Analyst {runId}-013` pada Position Name
39. Tekan Esc
40. Verifikasi dialog Unsaved Changes muncul dengan Body "You have unsaved changes. Are you sure you want to leave?"
41. Verifikasi dialog menampilkan tombol `[Cancel]` dan `[Leave]`
42. Verifikasi popup tidak langsung tertutup

### TC-GS-POS-61: Klik backdrop saat form terisi

43. Klik `[Cancel]` pada dialog Unsaved Changes
44. Klik area backdrop di luar popup
45. Verifikasi popup tetap terbuka
46. Verifikasi Position Name tetap berisi `Risk Analyst {runId}-013`
47. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-POS-62: Reload tab saat form terisi memunculkan konfirmasi browser

48. Tekan F5 dengan penanganan dialog `beforeunload` aktif
49. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul sebelum halaman di-reload
50. Tolak konfirmasi browser agar tetap di halaman

### TC-GS-POS-64: Pindah menu in-app saat form terisi

51. Klik menu sidebar Global Settings > General Settings
52. Verifikasi navigasi dicegat: dialog Unsaved Changes muncul
53. Verifikasi Body dialog menampilkan "You have unsaved changes. Are you sure you want to leave?"
54. Klik `[Cancel]`
55. Verifikasi tetap di Popup Create
56. Verifikasi Position Name tetap berisi `Risk Analyst {runId}-013`
57. Klik menu sidebar Global Settings > General Settings lagi
58. Verifikasi dialog Unsaved Changes tampil
59. Klik `[Leave]`
60. Verifikasi berpindah ke Global Settings > General Settings
61. Buka Global Settings > User > Position
62. Ketik Search `Risk Analyst {runId}-013`, tekan Enter
63. Verifikasi area tabel menampilkan Title "No results found"
64. Verifikasi tidak ada record `Risk Analyst {runId}-013` di tabel
65. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 55, 56, 57, 58, 59, 63, 60, 61, 62, 64. Urutan ini menyimpang dari urutan TC sumber (TC-GS-POS-63 setelah 62). Alasan: TC-GS-POS-63 memuat ulang halaman dengan form bersih dan menutup form, sehingga ditaruh sebelum rangkaian form terisi yang berlanjut pada satu pembukaan (60, 61, 62, 64).
- Pembukaan form (`[+ Position]`) dan kejadian menutup form: lima pembukaan (langkah 1, 5, 9, 32, 37) dan lima penutupan: ✕ bersih (langkah 2), Esc bersih (langkah 6), `[Leave]` (langkah 24), reload bersih (langkah 33), dan `[Leave]` pada pindah menu (langkah 59). TC-GS-POS-57 dan 58 berbagi satu pembukaan dengan TC-GS-POS-59 (✕ dua kali pada form yang sama); TC-GS-POS-60, 61, 62, dan 64 berbagi satu pembukaan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 28 dan 62 (Search agar pengecekan tabel bermakna), langkah 31 dan 65 (menutup input Search dan mereset tabel), langkah 43 (menutup dialog TC-GS-POS-60 lewat `[Cancel]` agar backdrop TC-GS-POS-61 diuji pada popup yang terbuka), langkah 50 (menolak konfirmasi browser agar form terisi tetap terbuka untuk TC-GS-POS-64), dan langkah 61 (kembali ke Position).
- Langkah 23 dan 58 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-59 dan TC-GS-POS-64 (dialog tampil sebelum `[Leave]` diklik, sesuai ketentuan menutup form dirty yang deterministik); langkah 35 dan 36 mengasersi bahwa halaman benar-benar ter-reload (tabel Position tampil pada langkah 35 sebagai anchor positif, lalu Popup Create hilang pada langkah 36) sebagai bukti "halaman langsung reload" pada Expected TC-GS-POS-63; langkah 61 sampai 64 mengamati "tidak ada record `Risk Analyst`" pada Expected c TC-GS-POS-64 dari tabel Position. Langkah 29 dan 63 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-59 dan TC-GS-POS-64: empty state "No results found" yang diproses Search menjadi anchor positif bagi asersi absence pada langkah 30 dan 64 (butir 2 bagian 8b konvensi).
- Spec melewati sekitar 35 langkah (65 langkah). Seluruhnya satu kelas (penutupan form Create), satu akun, tanpa membuat data; tiap blok TC dimulai dari pembukaan form sendiri (atau rangkaian terisi yang tetap bermakna bila blok lain gagal).
- Temuan untuk QA:
  - TC-GS-POS-62 tidak menyebut hasil setelah konfirmasi browser dijawab; spec menolak konfirmasi (tetap di halaman) supaya form dipakai TC-GS-POS-64.
  - Post Condition "Tidak ada record baru" pada TC-GS-POS-58 tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-POS-57 menyebut severity warning dan gaya tombol tanpa token style persis; asersi mengikuti kata-kata TC.
  - TC-GS-POS-64 Step 5 menyebut "menu sidebar yang sama lagi" tanpa menyebut bahwa dialog tampil kembali; spec mengasumsikan dialog tampil lagi (langkah 58) karena Step 6 mengklik `[Leave]`.
