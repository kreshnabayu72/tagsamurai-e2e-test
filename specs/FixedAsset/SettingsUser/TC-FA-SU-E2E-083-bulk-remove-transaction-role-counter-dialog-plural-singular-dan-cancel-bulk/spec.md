---
id: TC-FA-SU-E2E-083-bulk-remove-transaction-role-counter-dialog-plural-singular-dan-cancel-bulk
title: "Bulk Remove Transaction Role: Counter, Dialog Plural, Singular, dan Cancel Bulk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-267
  - TC-FA-SU-268
  - TC-FA-SU-1048
coverage:
  web: automated
---

# Bulk Remove Transaction Role: Counter, Dialog Plural, Singular, dan Cancel Bulk

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: kedua baris dihapus bersama (TC-FA-SU-267); satu baris Disposal × Staff dipilih (TC-FA-SU-268); kedua baris dipilih lalu dibatalkan (TC-FA-SU-1048).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini (kedua baris dihapus oleh TC-FA-SU-267); dipulihkan ke Pre-setup #39 lewat seed API pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-267: Bulk Remove beberapa baris: counter, dialog plural, toast token Role, dan log per baris

1. Catat jumlah entri `Remove` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
2. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role dan centang dua baris (Disposal × Staff dan Borrowing & Assignment × Approver)
3. Verifikasi counter `2 Transaction Roles selected` dan `[Bulk Remove]` tampil di Bulk Actions Bar
4. Klik `[Bulk Remove]`
5. Verifikasi dialog Title `Remove Transaction Roles` dengan Body `• Mira Anggraini`, `This user will lose the selected transaction roles.`, dan `Are you sure you want to remove them?`
6. Klik `[Remove]` pada dialog
7. Verifikasi toast "Success, Transaction Role has been removed." (Role pada kedua baris berbeda)
8. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
9. Verifikasi satu entri `Remove` per (Jenis Transaksi × Group × Role), dua entri bertambah dibanding baseline pada Tab Changelog

### TC-FA-SU-268: Bulk Remove seleksi satu baris memakai dialog dan counter singular

10. Pulihkan Transaction Role Mira Anggraini ke Pre-setup #39 lewat seed API
11. Buka ulang Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role dan centang satu baris (Disposal × Staff)
12. Klik `[Bulk Remove]`
13. Verifikasi counter `1 Transaction Role selected`
14. Verifikasi dialog Title `Remove Transaction Role` (singular) dengan `Are you sure you want to remove it?`
15. Klik `[Cancel]` pada dialog

### TC-FA-SU-1048: Cancel dialog Bulk Remove Transaction Role: tidak ada perubahan dan seleksi dipertahankan

16. Catat jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
17. Centang baris kedua (Borrowing & Assignment × Approver) sehingga dua baris terpilih
18. Klik `[Bulk Remove]` lalu klik `[Cancel]` pada dialog
19. Verifikasi dialog Title `Remove Transaction Roles` ditutup oleh `[Cancel]`
20. Verifikasi kedua baris tetap ada dengan seleksi dan Bulk Actions Bar dipertahankan
21. Verifikasi tidak ada toast
22. Klik `[Bulk Remove]` lalu tutup dialog dengan `[×]`
23. Verifikasi dialog Title `Remove Transaction Roles` ditutup oleh `[×]`
24. Verifikasi kedua baris tetap ada dengan seleksi dan Bulk Actions Bar dipertahankan
25. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang
26. Verifikasi jumlah entri Object `Transaction Role` Mira Anggraini pada Tab Changelog sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 10, 15 dan 16. Pemulihan lewat seed API memulihkan kedua baris yang dihapus TC-FA-SU-267 sebelum TC-FA-SU-268 dan 1048 mengandalkannya (S-09); `[Cancel]` pada TC-FA-SU-268 menutup dialog sebelum TC-FA-SU-1048 memakai seleksi yang sama; baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 8, 9, 25 dan 26. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-1048: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12); dialog menutup dan seleksi dipertahankan menjadi anchor positif.
- Temuan untuk QA:
  - TC-FA-SU-267 butir c memuat dua kasus toast (Role berbeda dan Role sama, contoh dua baris Approver) tetapi Data Uji hanya memuat dua baris dengan Role berbeda; kasus Role sama tidak diasersi.
  - TC-FA-SU-268 tidak menyebut hasil konfirmasi; dialog ditutup dengan `[Cancel]` sebagai langkah penghubung sehingga Post Condition "baris terpilih tidak ada setelah dikonfirmasi" tidak diasersi. Post Condition TC-FA-SU-267 (tiga permukaan log, Settings > Role & Permission) tidak punya langkah observasi tambahan di TC dan tidak diasersi.
