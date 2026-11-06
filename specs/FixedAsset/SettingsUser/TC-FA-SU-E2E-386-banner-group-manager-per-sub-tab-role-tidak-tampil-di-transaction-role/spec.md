---
id: TC-FA-SU-E2E-386-banner-group-manager-per-sub-tab-role-tidak-tampil-di-transaction-role
title: "Banner Group Manager per Sub-tab Role: Tampil di Global Role, Group Role, dan Transaction Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1074
coverage:
  web: automated
---

# Banner Group Manager per Sub-tab Role: Tampil di Global Role, Group Role, dan Transaction Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23).
- Pengguna target: Oscar Pranata (Pre-setup #9): Group Manager IT Infrastructure dan Accounts Payable, memegang baris pola Group Manager (Group Role katalog dan Transaction Role Asset Admin serta Approver), bukan Total Control atau Read Only; Qori Akbar (Pre-setup #4): Group Manager IT Infrastructure, Global Role Manage global user & role aktif, bukan Total Control atau Read Only.
- Data uji: tanpa data yang dibuat atau diubah; spec hanya membaca. Parameter blok berulang:

| Target | Banner Group Manager yang diharapkan di Sub-tab Global Role, Group Role, dan Transaction Role |
|---|---|
| Oscar Pranata | `This user is a Group Manager for: Accounts Payable, IT Infrastructure.` |
| Qori Akbar | `This user is a Group Manager for: IT Infrastructure.` |

- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1074: Banner Group Manager tampil di Sub-tab Global Role, Group Role, dan Transaction Role bagi user Group Manager yang bukan Total Control/Read Only

1. Ketik Search `Oscar Pranata`, tekan Enter, lalu klik Name `Oscar Pranata`
2. Klik Tab Role lalu Sub-tab Group Role
3. Verifikasi banner `This user is a Group Manager for: Accounts Payable, IT Infrastructure.` tampil (urut A-Z)
4. Klik Sub-tab Global Role
5. Verifikasi banner `This user is a Group Manager for: Accounts Payable, IT Infrastructure.` tampil (urut A-Z)
6. Klik Sub-tab Transaction Role
7. Verifikasi banner `This user is a Group Manager for: Accounts Payable, IT Infrastructure.` tampil di atas tabel Transaction Role (FI-20)
8. Verifikasi tabel Transaction Role memuat baris pola Asset Admin dan Approver
9. Verifikasi tidak ada banner `This user has Total Control access.` maupun `This user has Read Only access.` pada ketiga sub-tab
10. Kembali ke daftar User lewat Breadcrumb
11. Ganti isi kotak search dengan `Qori Akbar`, tekan Enter, lalu klik Name `Qori Akbar`
12. Klik Tab Role lalu Sub-tab Global Role
13. Verifikasi banner `This user is a Group Manager for: IT Infrastructure.` tampil
14. Klik Sub-tab Group Role
15. Verifikasi banner `This user is a Group Manager for: IT Infrastructure.` tampil
16. Klik Sub-tab Transaction Role
17. Verifikasi banner `This user is a Group Manager for: IT Infrastructure.` tampil
18. Verifikasi tidak ada banner `This user has Total Control access.` maupun `This user has Read Only access.` pada ketiga sub-tab

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 10 dan 11. Search pada langkah 1 dan 11 adalah langkah penghubung untuk menemukan baris target (R-16, R-23).
- Asersi "tidak ada banner" (langkah 9 dan 18) didahului `Verifikasi` banner Group Manager tampil pada ketiga sub-tab pengguna yang sama sebagai anchor positif (langkah 3, 5, 7 dan 13, 15, 17; 8b butir 2).
- Langkah 9 dan 18 memeriksa ketiga sub-tab; tidak ada banner tier di samping banner Group Manager yang sudah diverifikasi pada tiap sub-tab.
- Expected b TC-FA-SU-1074 (baris pola Asset Admin dan Approver pada tabel Transaction Role Oscar Pranata) diasersi pada langkah 8 saja; Expected c untuk Qori Akbar hanya menyebut banner, sehingga isi tabel Transaction Role Qori Akbar tidak diasersi.
- TC-FA-SU-1072 dan TC-FA-SU-1080 (banner tier Total Control dan Read Only) ada di spec 381.
- Temuan untuk QA:
  - TC-FA-SU-1074 menyebut ACC Role Total Control tanpa menyebut nama akun; spec memakai Total Control Lina Marlina (Pre-setup #1, akun default suite).
  - TC-FA-SU-1074 langkah 3 meminta mengamati "isi tabel" Sub-tab Transaction Role untuk kedua pengguna, tetapi Expected hanya menyebut isi tabel untuk Oscar Pranata (baris pola Asset Admin dan Approver) dan tidak menyebut jumlah barisnya; spec tidak mengasersi isi tabel Qori Akbar dan tidak mengasersi jumlah baris.
