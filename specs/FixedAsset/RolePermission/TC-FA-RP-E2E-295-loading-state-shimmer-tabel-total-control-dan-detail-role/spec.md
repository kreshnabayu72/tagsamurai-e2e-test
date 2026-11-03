---
id: TC-FA-RP-E2E-295-loading-state-shimmer-tabel-total-control-dan-detail-role
title: "Loading state tabel memakai Shimmer pada Tab Total Control dan Detail Role"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-72
coverage:
  web: automated
---

# Loading state tabel memakai Shimmer pada Tab Total Control dan Detail Role

## Prerequisites

- Mode: FE+BE. Respons baca ditunda (`Spectra.intercept()` pada respons nyata) hanya untuk mengamati state loading; respons dilepas segera sesudah asersi (S-09) dan data berasal dari backend nyata. Endpoint yang ditunda tidak tercantum di TC; nama endpoint ditentukan tim FE dari respons yang disebut TC (daftar user dan penugasan role).
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna). Spec hanya membaca; tidak mengubah data atau state global.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE): menunda respons HTTP pada surface yang disebut tiap langkah dan melepasnya; hook `after` melepas tunda yang tersisa.

## Test Steps

### TC-FA-RP-72: Loading state tabel memakai Shimmer

1. Pasang tunda pada respons daftar user, lalu muat ulang Tab `Total Control`
2. Verifikasi selama respons tertunda area tabel menampilkan Shimmer
3. Verifikasi area tabel bukan empty state maupun error
4. Lepas tunda pada respons daftar user
5. Verifikasi data tampil setelah respons datang
6. Klik Tab `System`
7. Pasang tunda pada respons penugasan role, lalu klik Role Name `Manage Open API`
8. Verifikasi selama respons tertunda area tabel Detail Role menampilkan Shimmer
9. Verifikasi area tabel Detail Role bukan empty state maupun error
10. Lepas tunda pada respons penugasan role
11. Verifikasi data Detail Role tampil setelah respons datang

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-72). TC-FA-RP-12, 13, 14, 73, dan 74 ada di spec `TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2`.
- Menahan respons hanya untuk mengamati state loading bukan kelas b (bagian 3 prinsip 13b); spec ini fungsional (`P-2` tidak diperlukan karena penundaan adalah objek asersi state UI, bukan kegagalan yang dipaksa).
- Langkah penghubung (tanpa awalan `Verifikasi`): pasang dan lepas tunda; klik Tab `System`. Asersi Shimmer diletakkan sebelum tunda dilepas (8b butir 5).
- Temuan untuk QA:
  - TC-FA-RP-72 expected a menyebut "bukan empty state maupun error"; spec memverifikasinya sebagai satu klausa per surface.
  - Post Condition TC-FA-RP-72 tidak memberi langkah observasi tambahan; tidak diasersi.
