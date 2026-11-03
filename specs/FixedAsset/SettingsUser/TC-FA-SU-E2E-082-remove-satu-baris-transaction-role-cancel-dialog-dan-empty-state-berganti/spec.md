---
id: TC-FA-SU-E2E-082-remove-satu-baris-transaction-role-cancel-dialog-dan-empty-state-berganti
title: "Remove Satu Baris Transaction Role, Cancel Dialog, dan Empty State Berganti"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-265
  - TC-FA-SU-266
  - TC-FA-SU-1050
coverage:
  web: automated
---

# Remove Satu Baris Transaction Role, Cancel Dialog, dan Empty State Berganti

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting) untuk TC-FA-SU-265 dan 266; Oscar Pranata tanpa Transaction Role untuk TC-FA-SU-1050.
- Data uji: baris Borrowing & Assignment × Approver dihapus (TC-FA-SU-265); baris Disposal × Staff dibatalkan penghapusannya (TC-FA-SU-266); Disposal × Staff pada Finance & Accounting ditambahkan lalu dihapus untuk Oscar Pranata (TC-FA-SU-1050).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini (satu baris dihapus) dan Oscar Pranata (ditambah lalu dihapus); dipulihkan ke Pre-setup #39 lewat seed API di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-265: Remove satu baris Transaction Role: dialog singular, toast removed, dan log Remove per grup

1. Catat jumlah entri `Remove` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
2. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `⋯` pada baris Borrowing & Assignment × Approver, lalu klik `Remove`
3. Verifikasi dialog Title `Remove Transaction Role` dengan Body bullet `• Mira Anggraini`, kalimat `This user will lose the selected transaction role.`, dan `Are you sure you want to remove it?`
4. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` (filled danger)
5. Klik `[Remove]` pada dialog
6. Verifikasi toast "Success, Approver has been removed."
7. Verifikasi baris Borrowing & Assignment × Approver hilang dari tabel
8. Verifikasi tidak ada dialog Auto-Revert tier
9. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
10. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Borrowing & Assignment — Finance & Accounting — Approver` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab Changelog

### TC-FA-SU-266: Cancel dialog Remove Transaction Role: tidak ada perubahan

11. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
12. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `⋯` pada baris Disposal × Staff, lalu klik `Remove`
13. Klik `[Cancel]`
14. Verifikasi dialog menutup
15. Verifikasi baris Disposal × Staff tetap ada
16. Verifikasi tidak ada toast
17. Klik `⋯` pada baris Disposal × Staff, klik `Remove`, lalu klik `[×]`
18. Verifikasi dialog menutup
19. Verifikasi baris Disposal × Staff tetap ada
20. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
21. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

### TC-FA-SU-1050: Empty state Sub-tab Transaction Role berganti sesuai penugasan: assign pertama dan hapus baris terakhir

22. Buka Detail Oscar Pranata > Tab Role > Sub-tab Transaction Role
23. Verifikasi empty state `No transaction role yet` dengan Description `Transaction roles assigned to this user will appear here.`
24. Klik `[+ Assign]`, pilih Group Finance & Accounting, Transaction Disposal, Role Staff, lalu klik `[Submit]`
25. Verifikasi empty state hilang
26. Verifikasi tabel menampilkan satu baris Disposal × Staff
27. Klik `⋯` pada baris Disposal × Staff, pilih `Remove`, lalu klik `[Remove]`
28. Verifikasi empty state `No transaction role yet` tampil kembali

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1 dan 11. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 9, 10, 20 dan 21. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-266: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); dialog menutup dan baris tetap ada menjadi anchor positif.
- Temuan untuk QA:
  - TC-FA-SU-265 butir c menyebut log "per grup" tanpa menyebut permukaan; spec mengasersi Tab Changelog. Post Condition TC-FA-SU-265 (tiga permukaan log, Settings > Role & Permission) tidak punya langkah observasi tambahan di TC dan tidak diasersi.
  - TC-FA-SU-1050 tidak menyebut toast untuk Submit dan Remove; spec tidak mengasersi toast pada TC itu. Langkah Submit dan Remove yang hasilnya tidak diasersi langsung diikuti `Verifikasi` keadaan tabel sehingga tidak ada langkah penghubung "Tunggu aksi selesai".
