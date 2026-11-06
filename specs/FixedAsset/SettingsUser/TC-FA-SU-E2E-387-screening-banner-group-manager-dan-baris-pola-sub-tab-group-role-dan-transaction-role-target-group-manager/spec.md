---
id: TC-FA-SU-E2E-387-screening-banner-group-manager-dan-baris-pola-sub-tab-group-role-dan-transaction-role-target-group-manager
title: "Screening Banner Group Manager dan Baris Pola Sub-tab Group Role dan Transaction Role: Target Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1081
  - TC-FA-SU-1088
coverage:
  web: automated
---

# Screening Banner Group Manager dan Baris Pola Sub-tab Group Role dan Transaction Role: Target Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager `FaUserGM` (Pre-setup #48). Hook `before` memastikan fixture Pre-setup #48 sesuai kondisi awal lewat seed API (kemampuan disediakan tim BE/FE).
- Pengguna target: Putri Anggraeni (Pre-setup #48): Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal × Staff pada IT Infrastructure, dan Damaged × Monitoring & Report pada Branch Surabaya.
- Data uji: tanpa data yang dibuat atau diubah; spec hanya membaca.
- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1081: Sub-tab Group Role target Group Manager: baris pola pada node GM dan turunannya tampil biasa, banner Group Manager, dan baris Manage user & role non-pola

1. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
2. Klik Tab Role lalu Sub-tab Group Role
3. Verifikasi banner `This user is a Group Manager for: Finance & Accounting.` tampil di atas tabel
4. Verifikasi banner tanpa tombol aksi
5. Verifikasi enam role katalog selain Manage user & role (Manage asset & TAG, Manage asset license, Manage files, Manage group, Manage purchase, View asset value) memuat grup `Accounts Payable` dan `Finance & Accounting`
6. Verifikasi badge grup pada enam role tersebut berurut A-Z
7. Verifikasi tidak ada baris, kolom, atau tanda penanda pola tambahan
8. Verifikasi baris Manage user & role memuat `Finance & Accounting` saja
9. Klik `[Detail]` pada baris Manage files
10. Verifikasi popup Detail Manage files memuat baris Accounts Payable dan Finance & Accounting
11. Verifikasi popup Detail memuat centang C/R/U/D penuh sesuai kolom yang berlaku (dimensi tidak applicable tampil `—`)
12. Klik `[✕]` untuk menutup popup Detail
13. Klik `[Assign Group]` pada baris Manage files
14. Verifikasi popup Assign Group Role Manage files memuat baris Accounts Payable dan Finance & Accounting
15. Verifikasi popup Assign Group Role memuat centang C/R/U/D penuh sesuai kolom yang berlaku (dimensi tidak applicable tampil `—`)
16. Klik `[✕]` untuk menutup popup Assign Group Role

### TC-FA-SU-1088: Sub-tab Transaction Role target Group Manager: banner Group Manager dan baris pola Asset Admin serta Approver per Jenis Transaksi pada node GM dan turunannya

17. Klik Sub-tab Transaction Role
18. Verifikasi banner `This user is a Group Manager for: Finance & Accounting.` tampil di atas tabel
19. Verifikasi banner tanpa tombol aksi
20. Verifikasi total 20 baris terpaginasi 10 per halaman
21. Telusuri seluruh halaman Pagination tabel hingga seluruh 20 baris teramati
22. Verifikasi tabel memuat 18 baris pola: satu baris Asset Admin dan satu baris Approver untuk tiap sembilan Jenis Transaksi
23. Verifikasi kolom Group baris pola berisi badge `Accounts Payable` dan `Finance & Accounting`
24. Verifikasi tabel tanpa kolom atau tanda penanda pola
25. Verifikasi baris pola tidak memuat baris Staff atau Monitoring & Report
26. Verifikasi dua baris non-pola tampil biasa: Disposal × Staff (IT Infrastructure) dan Damaged × Monitoring & Report (Branch Surabaya)
27. Ketik Search `Asset Admin`, tekan Enter
28. Verifikasi tabel menyisakan sembilan baris pola Asset Admin
29. Verifikasi `[+ Assign]` Enabled
30. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kedua TC memakai target yang sama (Putri Anggraeni); TC-FA-SU-1088 melanjutkan dari halaman Detail yang sudah terbuka di TC-FA-SU-1081 tanpa membuka ulang.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 12, 16, 21, 30. Search pada langkah 1 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 12 dan 16 menutup popup (S-03). Langkah 21 menelusuri halaman Pagination agar baris pola dan non-pola pada halaman kedua teramati (R-22). Langkah 30 membersihkan Search (S-09).
- Asersi "tidak ada baris, kolom, atau tanda penanda" (langkah 7, 24) dan "tidak memuat baris Staff atau Monitoring & Report" (langkah 25) didahului `Verifikasi` baris pola tampil di surface yang sama (langkah 5, 22) sebagai anchor positif (8b butir 2).
- Langkah 4 dan 19 mengasersi banner tanpa tombol aksi sesuai Expected TC (FI-19, FI-20).
- Spec membaca saja; tidak ada state yang diubah (S-09 tidak relevan).
- TC-FA-SU-1085 ada di spec 388, TC-FA-SU-1089 ada di spec 389 dan 401, TC-FA-SU-1096 ada di spec 390.
- Temuan untuk QA:
  - TC-FA-SU-1081 dan TC-FA-SU-1088 mengacu Pre-setup #1, #20, #21, #23, #48 tetapi Putri Anggraeni (Pre-setup #48) tidak tertulis pada kolom aktor Pre-setup #1 sampai #13; Putri hanya target sehingga spec tidak membutuhkan kredensialnya (suite.md tidak mendaftarkan nama env password untuk Putri).
  - TC-FA-SU-1081 langkah 3 dan 4 (klik `[Detail]` dan `[Assign Group]` pada baris Manage files) tidak menyebut cara menutup popup; spec memakai `[✕]` (langkah 12 dan 16).
  - TC-FA-SU-1088 Expected butir c menyebut "total 20 baris terpaginasi (10 per halaman)"; spec membaca total dari Pagination (langkah 20) dan menelusuri semua halaman (langkah 21), tidak menurunkannya dari seeding.
