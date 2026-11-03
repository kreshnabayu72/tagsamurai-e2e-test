---
id: TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1
title: "Resilience baca: Error load dan Try Again per permukaan (1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-64
  - TC-FA-RP-65
  - TC-FA-RP-66
  - TC-FA-RP-67
  - TC-FA-RP-68
coverage:
  web: automated
---

# Resilience baca: Error load dan Try Again per permukaan (1/2)

## Prerequisites

- Mode: FE+BE. Intercept parsial (`Spectra.intercept()`) di atas backend nyata: hanya respons baca yang disebut TC yang dipaksa berstatus 5xx; respons lain dan respons setelah intercept dilepas berasal dari backend nyata, karena TC mengharapkan `[Try Again]` memuat data nyata. Endpoint yang dicegat tidak tercantum di TC; nama endpoint ditentukan tim FE dari respons yang disebut TC (daftar user, daftar Group Manager, katalog role, penugasan role, penugasan Role Transaksi).
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna), #18 (pohon group), #19 (seed Role Transaksi pada `IT Infrastructure`), #43 (seed Group Manager).
- Kemampuan teknis (disediakan tim FE): intercept respons HTTP dengan status 5xx pada surface yang disebut tiap langkah, dilepas segera sesudah asersi (S-09); hook `after` melepas intercept yang tersisa.
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-FA-RP-64: Error load Tab Total Control

1. Pasang intercept respons daftar user dengan status 5xx, lalu muat ulang Tab `Total Control`
2. Verifikasi area konten menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
3. Verifikasi area konten bukan empty state
4. Verifikasi halaman tidak tertutup
5. Lepas intercept respons daftar user
6. Klik `[Try Again]`
7. Verifikasi data berhasil dimuat dan tampil normal

### TC-FA-RP-65: Error load Tab Group Manager

8. Pasang intercept respons daftar Group Manager dengan status 5xx, lalu klik Tab `Group Manager`
9. Verifikasi area konten menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
10. Verifikasi area konten bukan empty state
11. Verifikasi halaman tidak tertutup
12. Lepas intercept respons daftar Group Manager
13. Klik `[Try Again]`
14. Verifikasi data berhasil dimuat dan tampil normal

### TC-FA-RP-68: Error load tabel Role Transaksi

15. Klik Tab `Transaction Role`
16. Pasang intercept respons penugasan Role Transaksi dengan status 5xx, lalu klik node `IT Infrastructure`
17. Verifikasi area konten menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
18. Verifikasi area konten bukan empty state
19. Verifikasi halaman tidak tertutup
20. Lepas intercept respons penugasan Role Transaksi
21. Klik `[Try Again]`
22. Verifikasi data berhasil dimuat dan tampil normal

### TC-FA-RP-66: Error load Tab System

23. Pasang intercept respons katalog role dengan status 5xx, lalu klik Tab `System`
24. Verifikasi area konten menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
25. Verifikasi area konten bukan empty state
26. Verifikasi halaman tidak tertutup
27. Lepas intercept respons katalog role
28. Klik `[Try Again]`
29. Verifikasi data berhasil dimuat dan tampil normal

### TC-FA-RP-67: Error load Detail Role

30. Pasang intercept respons penugasan role dengan status 5xx, lalu klik Role Name `Manage Open API`
31. Verifikasi area konten menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
32. Verifikasi area konten bukan empty state
33. Verifikasi halaman tidak tertutup
34. Lepas intercept respons penugasan role
35. Klik `[Try Again]`
36. Verifikasi data berhasil dimuat dan tampil normal

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-64, 65, 66, 67, 68). TC-FA-RP-69, 70, dan 71 ada di spec `TC-FA-RP-E2E-018-resilience-baca-error-load-dan-try-again-per-permukaan-2`.
- Urutan TC di spec: TC-FA-RP-64, 65, 68, 66, 67, supaya Tab `Transaction Role` dikunjungi sebelum Tab `System` dan Detail Role dibuka terakhir tanpa perlu kembali ke daftar.
- Spec kelas b (resilience) satu pola untuk lima surface baca; tiap blok berdiri sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab dan node; memasang intercept sebagai pemicu kegagalan; melepas intercept segera sesudah asersi (S-09); klik `[Try Again]`.
- Alasan di atas sekitar 35 langkah (36 langkah): seluruh blok satu kelas harness (resilience baca) dan satu pola; kegagalan satu surface tidak membuat surface lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-64 sampai 68 memakai frasa "blokir respons"; spec memaknainya sebagai intercept respons 5xx (Status respons 5xx pada Data Uji TC). Nama endpoint yang dicegat tidak tercantum di TC.
  - TC-FA-RP-64 sampai 68 mengasersi `[Try Again]` memuat data nyata, sehingga spec ini FE+BE dengan intercept parsial, bukan `Mode: mock` penuh (bagian 6 konvensi).
  - Post Condition TC-FA-RP-64 sampai 68 tidak memberi langkah observasi tambahan; tidak diasersi.
