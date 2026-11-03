---
id: TC-FA-SU-E2E-352-defense-in-depth-assign-transaction-role-target-total-control-dan-read-only
title: "Defense-in-depth Transaction Role: Assign pada Target Total Control dan Read Only bagi Aktor Group dan Group Manager"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1061
coverage:
  web: automated
---

# Defense-in-depth Transaction Role: Assign pada Target Total Control dan Read Only bagi Aktor Group dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 12 Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Lina Marlina (Total Control dengan Transaction Role) dan Citra Lestari (Read Only). Semua blok hanya membaca dan permintaan ditolak server, sehingga tidak ada data yang diubah.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Ganti akun ke Oscar Pranata (langkah 12) memakai login UI; klien HTTP memakai token sesi API akun yang sama.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1061: Assign Transaction Role pada target Total Control dan Read Only

1. Ketik Search `Lina`, tekan Enter, klik nama Lina Marlina (Total Control), lalu buka Tab Role > Sub-tab Transaction Role
2. Hover `[+ Assign]`
3. Verifikasi `[+ Assign]` pada Lina Marlina tampil (Show) tetapi Disabled dengan tooltip "You don't have permission to edit."
4. Hover `[Assign Group]` pada baris Lina Marlina
5. Verifikasi `[Assign Group]` pada baris Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
6. Kembali ke User List, ketik Search `Citra`, tekan Enter, klik nama Citra Lestari (Read Only), lalu buka Tab Role > Sub-tab Transaction Role
7. Hover `[+ Assign]`
8. Verifikasi `[+ Assign]` pada Citra Lestari tampil (Show) tetapi Disabled dengan tooltip "You don't have permission to edit."
9. Kirim permintaan langsung ke API assign Transaction Role untuk Lina Marlina memakai klien HTTP dengan token sesi Sinta Dewi
10. Verifikasi server menolak permintaan dengan status 403
11. Verifikasi tidak ada perubahan data Transaction Role Lina Marlina (dibaca lewat API)
12. Ganti akun: logout, login sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`), lalu buka Fixed Asset > Settings > User; klien HTTP memakai token sesi API akun yang sama
13. Ketik Search `Lina`, tekan Enter, klik nama Lina Marlina (Total Control), lalu buka Tab Role > Sub-tab Transaction Role
14. Hover `[+ Assign]`
15. Verifikasi `[+ Assign]` pada Lina Marlina tampil (Show) tetapi Disabled dengan tooltip "You don't have permission to edit."
16. Hover `[Assign Group]` pada baris Lina Marlina
17. Verifikasi `[Assign Group]` pada baris Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
18. Kembali ke User List, ketik Search `Citra`, tekan Enter, klik nama Citra Lestari (Read Only), lalu buka Tab Role > Sub-tab Transaction Role
19. Hover `[+ Assign]`
20. Verifikasi `[+ Assign]` pada Citra Lestari tampil (Show) tetapi Disabled dengan tooltip "You don't have permission to edit."
21. Kirim permintaan langsung ke API assign Transaction Role untuk Lina Marlina memakai klien HTTP dengan token sesi Oscar Pranata
22. Verifikasi server menolak permintaan dengan status 403
23. Verifikasi tidak ada perubahan data Transaction Role Lina Marlina (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-1061 (butir c) berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- TC-FA-SU-1061 Expected a dan b (tampilan) diasersi lewat UI; Expected c (permintaan langsung) hanya status respons dan state data (bagian 8b butir 1). Iterasi kedua (langkah 12 sampai 23) mengulang langkah 1 sampai 11 untuk Group Manager sesuai Langkah Uji 5 TC.
- Search untuk menemukan baris target (R-16) dicatat sebagai langkah penghubung.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 6, 13, 18.
- Ganti akun eksplisit (S-07): langkah 12.
- Temuan untuk QA:
  - Klausa "tanpa perubahan data" Expected c TC-FA-SU-1061 diasersi lewat pembacaan state data karena TC tidak menyebut entri log; Post Condition "tidak ada entri log" tanpa langkah observasi tidak diasersi (S-01, S-05).
  - Email dan password Sinta Dewi (#6) dan Oscar Pranata (#9) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - Tooltip "You don't have permission to edit." dikutip dari Expected TC yang merujuk S-15; teks persisnya mengikuti Expected.
