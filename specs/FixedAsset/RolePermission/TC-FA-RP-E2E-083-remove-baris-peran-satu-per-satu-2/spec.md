---
id: TC-FA-RP-E2E-083-remove-baris-peran-satu-per-satu-2
title: "Remove baris peran satu per satu (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-283
  - TC-FA-RP-1016
coverage:
  web: automated
---

# Remove baris peran satu per satu (2/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Sesi API aktor: login API untuk pelaku kedua dan pembacaan state lewat fixture BE mengikuti pernyataan di suite.md.
- Pelaku kedua (Sesi 2) pada TC-FA-RP-283: Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD`, lewat sesi API (hanya memicu perubahan state, bukan konteks UI kedua).
- Data Pre-setup: pool #15 (Budi Santoso, Endah Susanti) dan #18. Budi Santoso memegang Global Role `Manage Open API`; Endah Susanti satu-satunya pemegang Group Role `View asset value` di `Data Center`. Disiapkan lewat seed API di hook `before` dan sebagai langkah penghubung (langkah 10).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Budi Santoso `Manage Open API` dan Endah Susanti `View asset value` di `Data Center`), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-283: Remove atas baris yang sudah hilang tetap selesai tanpa efek

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Verifikasi baris Budi Santoso tampil di Detail Role `Manage Open API` pada Sesi 1
3. Sesi 2 (sesi API Total Control Rina Wulandari) meng-Remove baris Budi Santoso pada Detail Role `Manage Open API` hingga penghapusan tersimpan
4. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
5. Di Sesi 1, klik `[⋯]` baris Budi Santoso lalu `Remove`, klik `[Remove]`
6. Verifikasi tindakan Sesi 1 selesai tanpa efek: dialog Remove tertutup
7. Verifikasi tidak muncul toast netral `This role assignment is no longer available.`
8. Verifikasi Detail Role `Manage Open API` termuat: judul Detail Role dan header tabel tampil
9. Verifikasi tabel Sesi 1 tidak memuat baris Budi Santoso

### TC-FA-RP-1016: Remove baris terakhir menuju empty state dan Assign keluar dari empty state

10. Pulihkan state lewat seed API: role `View asset value` hanya memiliki satu penugasan, Endah Susanti di `Data Center`
11. Klik Tab `System`, klik Role Name `View asset value` pada section Group Role
12. Klik `All Groups` di Sidebar Group Tree
13. Klik `[⋯]` baris Endah Susanti lalu `Remove`, klik `[Remove]`
14. Verifikasi muncul toast sukses: `Success, user has been removed.`
15. Verifikasi tabel menampilkan empty state: Title `No users assigned` dan Description `Assign users to grant them access with this capability.`
16. Klik `[+ Assign]`, pilih group `Data Center`
17. Centang Endah Susanti, klik `[Assign]`
18. Verifikasi muncul toast sukses: `Success, View asset value has been assigned.`
19. Verifikasi empty state hilang
20. Verifikasi baris Endah Susanti tampil dengan badge Group `Data Center`
21. Verifikasi Read tercentang Disabled
22. Verifikasi Create, Update, dan Delete menampilkan `—`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-283, TC-FA-RP-1016).
- Langkah penghubung (S-03): membuka Tab System dan Detail Role; "Tunggu aksi selesai" pada langkah 4 karena aktor berpindah sesi sesudah aksi tanpa asersi (bagian 8b butir 8); pemulihan state seed (langkah 10); memilih group `Data Center` pada popup Assign.
- Pembagian TC lintas spec: klausa "tanpa entri log tambahan" pada Expected a TC-FA-RP-283 diasersi di spec 291 (kelas g, absence log) dengan aksi nyata dan baseline sendiri; spec ini mengasersi klausa lain TC-FA-RP-283 (S-05).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` Detail Role termuat (langkah 8) sebagai anchor positif untuk asersi absence baris dan toast (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-283 menyebut "Dua sesi Total Control" tanpa akun sesi kedua; spec memakai Total Control kedua Pre-setup #3 lewat sesi API.
  - Expected TC-FA-RP-283 a menyebut "selesai tanpa efek" tanpa elemen yang teramati; spec mengamati dialog Remove tertutup tanpa perubahan baris.
