---
id: TC-AC-RP-E2E-064-toggle-require-approval-total-control
title: "Toggle Require Approval oleh Total Control: Allocation dan Wallet Allocation, OFF ke ON dan Sebaliknya, Independen per Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-216
  - TC-AC-RP-217
  - TC-AC-RP-218
  - TC-AC-RP-219
coverage:
  web: automated
---

# Toggle Require Approval oleh Total Control: Allocation dan Wallet Allocation, OFF ke ON dan Sebaliknya, Independen per Group

## Prerequisites

- Mode: FE+BE (penahanan respons lewat intercept di atas backend nyata untuk TC-AC-RP-216).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group `Region Jawa` dengan anak `Jakarta`, `Surabaya`; `Sumatera`), #17 (toggle `Manage allocation` `Region Jawa` ON, `Sumatera` OFF tersimpan, group lain tanpa nilai; `Manage wallet & pricing` seluruh group OFF).
- Data Dinamis: spec ini tidak membuat Data Dinamis; target aksi adalah toggle Pre-setup. Nilai bersuffix `+{runId}-064` tidak dipakai karena tidak ada data yang dibuat spec.
- Kemampuan teknis (Pre-setup #23): penundaan respons simpan toggle lewat intercept (TC-AC-RP-216) agar state sementara toggle "disabled selama proses" dapat diasersi sebelum respons dilepas.
- Perubahan Pre-setup: toggle `Manage wallet & pricing` `Region Jawa` (ON), `Manage allocation` `Region Jawa` (OFF), `Manage allocation` `Sumatera` (ON). Pemulihan ke nilai awal memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Changelog Role Detail menerima entri perubahan toggle; Last Updated berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-219: Toggle Require Approval for Wallet Allocation

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage wallet & pricing` lalu klik `Detail`
3. Klik node `Region Jawa`
4. Klik toggle "Require Approval for Wallet Allocation"
5. Verifikasi toggle "Require Approval for Wallet Allocation" ON
6. Verifikasi toast "Success, permissions have been updated."
7. Buka halaman `Settings > Role & Permission`
8. Klik tab `System`
9. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
10. Klik node `Region Jawa`
11. Verifikasi toggle "Require Approval for Allocation" `Manage allocation` tidak berubah (tetap ON)

### TC-AC-RP-218: Toggle Require Approval for Allocation ON ke OFF

12. Klik toggle "Require Approval for Allocation" (ON) sehingga OFF
13. Verifikasi toast "Success, permissions have been updated."
14. Muat ulang halaman
15. Klik node `Region Jawa`
16. Verifikasi nilai `Region Jawa` OFF setelah refresh

### TC-AC-RP-217: Toggle tersimpan independen per group

17. Klik node `Sumatera`
18. Klik toggle "Require Approval for Allocation" sehingga ON
19. Tunggu aksi selesai (toggle aktif kembali)
20. Klik node `Surabaya`
21. Verifikasi toggle `Surabaya` tetap OFF (nilai sendiri)
22. Klik node `Sumatera`
23. Verifikasi toggle `Sumatera` ON

### TC-AC-RP-216: Toggle Require Approval for Allocation OFF ke ON

24. Pulihkan baseline automation: toggle `Manage allocation` `Sumatera` kembali OFF, lalu muat ulang halaman
25. Klik node `Sumatera`
26. Tahan respons simpan toggle (intercept penundaan respons)
27. Klik toggle "Require Approval for Allocation"
28. Verifikasi toggle berubah ke ON langsung
29. Verifikasi toggle disabled selama proses
30. Lepas tahanan respons
31. Verifikasi toast "Success, permissions have been updated."
32. Verifikasi section Approvers tetap tampil tak berubah

## Notes

- Mode: FE+BE (penahanan respons). Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Perubahan urutan TC (S-05, S-10): urutan di spec 219, 218, 217, 216. Alasan: state toggle dibangun berurutan sehingga pemulihan baseline cukup satu kali. Group `Region Jawa` pada `Manage allocation` yang masih ON dipakai TC-AC-RP-219 dan TC-AC-RP-218 berurutan, lalu `Sumatera` (OFF) dipakai TC-AC-RP-217 dan TC-AC-RP-216 dengan satu pemulihan di langkah 24. Jumlah langkah tetap di bawah batas ±35.
- Langkah penghubung (S-03): langkah 7 sampai 10 (navigasi ke Role Detail `Manage allocation`), 14 dan 15 (muat ulang dan pilih ulang node untuk asersi sesudah refresh pada Expected), 19 (tunggu aksi selesai sebelum pindah node, bagian 8b butir 8), 24 (pemulihan baseline), 26 dan 30 (tahan dan lepas respons).
- Asersi state sementara (bagian 8b butir 5 dan 11): langkah 28 dan 29 ditulis sebelum respons dilepas (langkah 30); toast (langkah 31) sesudah respons dilepas.
- Temuan untuk QA:
  - TC-AC-RP-216 Expected "disabled selama proses" adalah state sementara yang tidak teramati tanpa penundaan respons; TC tidak menyebut cara menahan respons. Spec memakai penundaan respons (Pre-setup #23).
  - TC-AC-RP-217 Langkah 4 "ubah toggle ke ON" tidak menyebut Expected untuk toast; tidak diasersi.
  - TC-AC-RP-218 Expected "setelah refresh" tidak menyebut node yang dipilih; spec memilih ulang node `Region Jawa` sesudah muat ulang.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
