---
id: TC-GS-USER-E2E-024-create-sukses-field-wajib-semua-field-dan-variasi-access
title: "Create User Sukses: Field Wajib Saja, Semua Field Opsional Terisi, Access Global Settings Saja, dan Access Fixed Asset + Supply Asset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-117
  - TC-GS-USER-118
  - TC-GS-USER-119
  - TC-GS-USER-120
coverage:
  web: automated
---

# Create User Sukses: Field Wajib Saja, Semua Field Opsional Terisi, Access Global Settings Saja, dan Access Fixed Asset + Supply Asset

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca kecuali TAG; lihat state global):
  - Client PT Maju Bersama, plan Growth, subscription Fixed Asset dan Supply Asset (No. 26).
  - Master Data Position `Finance Manager` (No. 22); Division `Finance` dan `Logistics` (No. 23).
  - Custom Field aktif `Blood Type` (Dropdown A/B/O/AB), `Skills` (Multi-Dropdown Excel/SQL), `Emergency Phone` (Phone) (No. 24).
  - TAG `TAG-USR-0001` (user, aktif, bebas, belum dipasang) (No. 25).
- Data Dinamis (dibuat lewat UI oleh spec; tidak di-seed). Seluruhnya dihapus di hook `after` lewat API menurut Email, tanpa mengandalkan Submit berhasil penuh:
  - U-1 (TC-GS-USER-117): Name `Budi Santoso {runId}-024-117`, Email `budisantoso+{runId}-024-117@qwertysystem.net`, Emergency Phone (`🇮🇩 +62`, `81234567890`).
  - U-2 (TC-GS-USER-118): Name `Budi Santoso {runId}-024-118`, Email `budisantoso+{runId}-024-118@qwertysystem.net`, Position `Finance Manager`, Employee ID `EMP-0101-{runId}-024`, TAG `TAG-USR-0001`, Temporary Until hari ini + 30 hari, Blood Type `O`, Skills `Excel`, Emergency Phone `081234567890`, Photo `budi.png`.
  - U-3 (TC-GS-USER-119): Name `Sari Wulandari {runId}-024-119`, Email `sariwulandari+{runId}-024-119@qwertysystem.net`, Division `Logistics`, Emergency Phone (`🇮🇩 +62`, `81234567890`).
  - U-4 (TC-GS-USER-120): Name `Sari Wulandari {runId}-024-120`, Email `sariwulandari+{runId}-024-120@qwertysystem.net`, Division `Logistics`, Emergency Phone (`🇮🇩 +62`, `81234567890`).
- Berkas foto `budi.png` (fixture unggahan, disediakan tim FE).
- Pemulihan data Pre-setup yang ditulis spec ini (TAG `TAG-USR-0001`, status Required `Emergency Phone`) merujuk fixture pemulihan di `suite.md` ("Pemulihan data Pre-setup yang ditulis spec").
- State global yang diubah:
  - TAG `TAG-USR-0001` dipasang ke U-2 (TC-GS-USER-118). Hook `after` memastikan TAG itu kembali bebas dan belum dipasang (lewat penghapusan U-2 atau Unpair); mekanisme pelepasan TAG tidak disebut di TC dan PRD, disediakan tim FE/BE.
  - Custom Field `Emergency Phone` tidak Required selama spec ini (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158 dan 349, TC Create dan Edit lain dijalankan saat Required nonaktif; TC-GS-USER-117, 119, 120 tetap mengisinya sesuai TC, dan TC-GS-USER-118 mengisinya `081234567890`; status Required nonaktif tetap dipertahankan sesuai kesepakatan). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah.
  - Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE bila belum ada): simulasi scan TAG `TAG-USR-0001` pada tombol `Scan TAG` (TC tidak menyebut mekanismenya); unggah berkas ke Photo; memilih tanggal Temporary Until; membaca Timezone dan Date Format client (General Settings) untuk menghitung dan memformat "hari ini + 30 hari"; Search di User List menurut Name (kolom yang dicari ditentukan tim FE).

## Test Steps

### TC-GS-USER-117: Create happy path, field wajib saja

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik `[+ User]` di Table Tools
3. Isi First Name `Budi`, Last Name `Santoso {runId}-024-117`, Division `Finance`, Email `budisantoso+{runId}-024-117@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
4. Klik `[Submit]`
5. Verifikasi Popup tertutup
6. Verifikasi toast sukses: "Success, user has been created."
7. Klik icon Search, ketik `{runId}-024-117`, tekan Enter
8. Verifikasi baris `Budi Santoso {runId}-024-117`: switch Active ON
9. Verifikasi baris `Budi Santoso {runId}-024-117`: badge `Pending Activation`
10. Verifikasi baris `Budi Santoso {runId}-024-117`: Position `—`
11. Verifikasi baris `Budi Santoso {runId}-024-117`: Division `Finance`
12. Verifikasi baris `Budi Santoso {runId}-024-117`: Access `Fixed Asset`
13. Verifikasi baris `Budi Santoso {runId}-024-117`: Employee ID `—`
14. Verifikasi baris `Budi Santoso {runId}-024-117`: Modified By `Siti N`
15. Buka Detail Budi Santoso {runId}-024-117
16. Verifikasi Detail: badge `Active` dan `Pending Activation`
17. Verifikasi Detail: User Type `Basic`
18. Verifikasi Detail: User TAG `Unverified` dan `No TAG paired`
19. Verifikasi Detail: Authenticator `Not enrolled yet`
20. Verifikasi Detail: tanpa info Temporary

### TC-GS-USER-119: Create dengan Access Global Settings saja

21. Buka Global Settings > User > User List lewat sidebar (sub-tab Login User)
22. Klik `[+ User]` di Table Tools
23. Isi First Name `Sari`, Last Name `Wulandari {runId}-024-119`, Division `Logistics`, Email `sariwulandari+{runId}-024-119@qwertysystem.net`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
24. Pilih Access `Global Settings` saja
25. Klik `[Submit]`
26. Verifikasi toast sukses: "Success, user has been created."
27. Refresh halaman
28. Klik icon Search, ketik `{runId}-024-119`, tekan Enter
29. Buka Detail Sari Wulandari {runId}-024-119
30. Verifikasi Detail: Access `Global Settings`
31. Verifikasi Detail: User Type `Basic`
32. Verifikasi Detail: tanpa tier dan tanpa role
33. Verifikasi Detail: badge `Active` dan `Pending Activation`

### TC-GS-USER-120: Create dengan Access Fixed Asset dan Supply Asset tanpa Global Settings

34. Buka Global Settings > User > User List lewat sidebar (sub-tab Login User)
35. Klik `[+ User]` di Table Tools
36. Isi First Name `Sari`, Last Name `Wulandari {runId}-024-120`, Division `Logistics`, Email `sariwulandari+{runId}-024-120@qwertysystem.net`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
37. Pilih Access `Fixed Asset` dan `Supply Asset`
38. Klik `[Submit]`
39. Verifikasi toast sukses: "Success, user has been created."
40. Refresh halaman
41. Klik icon Search, ketik `{runId}-024-120`, tekan Enter
42. Verifikasi baris `Sari Wulandari {runId}-024-120`: switch Active tetap ON
43. Buka Detail Sari Wulandari {runId}-024-120
44. Verifikasi Detail: Access `Fixed Asset` dan `Supply Asset`
45. Verifikasi Detail: badge `Active` dan `Pending Activation`

### TC-GS-USER-118: Create dengan semua field opsional terisi

46. Buka Global Settings > User > User List (sub-tab Login User)
47. Klik `[+ User]` di Table Tools
48. Upload Photo `budi.png`
49. Isi First Name `Budi`, Last Name `Santoso {runId}-024-118`, Division `Finance`, Email `budisantoso+{runId}-024-118@qwertysystem.net`, pilih Access `Fixed Asset`
50. Isi Position `Finance Manager`, Employee ID `EMP-0101-{runId}-024`
51. Klik `Scan TAG`, scan `TAG-USR-0001`
52. Centang `Set as Temporary User`, Temporary Until = hari ini + 30 hari
53. Pilih Custom Field `Blood Type` = `O`, `Skills` = `Excel`, isi `Emergency Phone` `081234567890`
54. Klik `[Submit]`
55. Verifikasi toast sukses: "Success, user has been created."
56. Verifikasi tidak ada toast Pair TAG terpisah
57. Klik icon Search, ketik `{runId}-024-118`, tekan Enter
58. Verifikasi baris `Budi Santoso {runId}-024-118`: switch Active ON
59. Verifikasi baris `Budi Santoso {runId}-024-118`: badge `Pending Activation`
60. Buka Detail Budi Santoso {runId}-024-118
61. Verifikasi Detail: Avatar menampilkan foto
62. Verifikasi Detail: Position `Finance Manager`
63. Verifikasi Detail: Employee ID subtitle `EMP-0101-{runId}-024`
64. Verifikasi Detail: User TAG badge `Verified`
65. Verifikasi Detail: User TAG `TAG-USR-0001`
66. Verifikasi Detail: info `Temporary until` menampilkan tanggal hari ini + 30 hari
67. Verifikasi Detail: Custom Field `Blood Type` = `O`
68. Verifikasi Detail: Custom Field `Skills` = `Excel`
69. Verifikasi Detail: Custom Field `Emergency Phone` = `081234567890`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-USER-118 (memakai simulator scan `TAG-USR-0001` di langkah 51) dipindah ke akhir spec (langkah 46 sampai 69), sesudah TC-GS-USER-117, 119, dan 120, supaya kegagalan simulator tidak menutupi blok yang tidak membutuhkan hardware (konvensi bagian 3, pemisah nyata hardware berisiko). Pemisahan blok simulator scan (konvensi bagian 3, pemisah nyata hardware berisiko): objek uji TC-GS-USER-118 adalah Create dengan semua field opsional terisi, bukan perangkat scan; scan hanya membentuk state TAG terpasang yang diasersi sesudah Submit. Antar blok tidak ada state yang perlu dipulihkan (tiap blok membuat user sendiri dan membuka layar sendiri). Spec tidak menghapus data di langkah; seluruh user dihapus di hook `after`. Spec tidak memuat validasi diblokir.
- Spec melewati sekitar 35 langkah (69 langkah) karena seluruh blok berada di satu kelas harness (Create sukses, tanpa harness eksternal), tiap blok membuat user sendiri dan berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan Expected dipecah per klausa (S-01). Pembukaan layar yang berulang per blok tidak dihitung.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): membuka User List dan `[+ User]` di awal tiap blok; Search menurut `{runId}-024-<TC>` untuk menemukan baris user uji sebelum membuka Detail dan memeriksa baris; `Refresh halaman` pada TC-GS-USER-119 dan 120 mengikuti langkah TC.
- Verifikasi switch Active dan badge `Pending Activation` pada TC-GS-USER-118 diamati di baris User List sebelum Detail dibuka (padanan Expected c "sama seperti Create field wajib saja", yang memeriksa baris User List pada TC-GS-USER-117).
- Verifikasi switch Active ON pada TC-GS-USER-120 diamati di baris User List sesudah Refresh halaman.
- TC-GS-USER-117 Expected c memeriksa baris User List dengan ketujuh kolom disebut utuh; tiap kolom memiliki `Verifikasi` sendiri (S-01).
- Post Condition tanpa langkah observasi di TC tidak diasersi (S-01, S-15): TC-GS-USER-117 (role default User Basic di Fixed Asset, Activation Email dikirim dan cooldown resend 60 detik, dampak ke Fixed Asset > Settings > User dan modul Auth) dan TC-GS-USER-118 (dampak ke TAG Registry dan Hardware > Handheld > Detail).
- Temuan untuk QA:
  - TC-GS-USER-117, 119, 120 mengisi `Emergency Phone` (`🇮🇩 +62`, `81234567890`) pada Langkah Uji dan spec mengisinya; Tabel Pre-setup No. 24 menyatakan Required hanya aktif untuk TC-GS-USER-158 dan 349, sehingga Required tetap nonaktif selama spec (disediakan tim FE/BE). Langkah Uji TC-GS-USER-120 menulis pengisian `Emergency Phone` di tengah kalimat pemilihan Access ("pilih Access `Fixed Asset`, isi Emergency Phone ... dan `Supply Asset`"); spec mengisinya bersama field wajib pada langkah 36.
  - TC-GS-USER-117 dan 118 memakai Email `budisantoso@qwertysystem.net` yang sama; Email unik global, sehingga kedua user tidak dapat ada bersamaan. Spec memakai suffix `{runId}-024-<TC>` per user; hal yang sama berlaku untuk TC-GS-USER-119 dan 120 (`sariwulandari@qwertysystem.net`).
  - TC-GS-USER-118 Expected c menyebut "Switch Active ON" tanpa menyebut permukaannya (User List atau Detail); spec memeriksa baris User List.
  - TC-GS-USER-118 Expected b menyebut "Avatar foto" dan "info `Temporary until [tanggal]`" tanpa format tanggal; spec memakai Date Format General Settings client.
  - TC-GS-USER-118 mensyaratkan TAG `TAG-USR-0001` "diaktivasi dan belum dipasang" (Tabel Pre-setup No. 25, data bersama) dan memasangnya ke user baru, sehingga mengubah data Pre-setup (S-06). Pemulihan lewat hook `after` disediakan tim FE/BE.
  - TC-GS-USER-118 menyebut "scan `TAG-USR-0001`" tanpa mekanisme simulasi scan; disediakan tim FE/BE.
  - TC-GS-USER-117, 119, 120 menyebut "Buka Detail" dan "Refresh halaman, buka Detail" tanpa cara menemukan baris; spec memakai Search menurut `{runId}-024-<TC>`.
  - TC-GS-USER-117 Post Condition: Activation Email dikirim dan cooldown resend 60 detik; TC tidak memberi langkah observasi (tidak diasersi).
