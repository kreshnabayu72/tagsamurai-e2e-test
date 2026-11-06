---
id: TC-FA-SU-E2E-390-kolom-role-popup-role-count-filter-dan-search-user-group-manager-baris-pola-tanpa-badge
title: "Kolom Role, Popup Role Count, Filter, dan Search User Group Manager: Baris Pola Tanpa Badge"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1096
coverage:
  web: automated
---

# Kolom Role, Popup Role Count, Filter, dan Search User Group Manager: Baris Pola Tanpa Badge

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23) dan atribut User List (Pre-setup #43). Hook `before` tidak membutuhkan varian `FaUserGM` (Pre-setup #48); TC mengacu Pre-setup #9 (lihat Temuan untuk QA).
- Pengguna target: Oscar Pranata (Pre-setup #9): Group Manager IT Infrastructure dan Accounts Payable dengan baris pola Group Manager; Qori Akbar (Pre-setup #4 dan #23): Global Role Manage global user & role aktif dan Group Manager IT Infrastructure dengan baris pola pada IT Infrastructure. Angka Role turunan (`48 roles`, `25 roles`) tidak diasersi eksak karena perilaku hitung menunggu keputusan PM (PRD Open Item 3); spec mengasersi bentuk label dan kesamaan label dengan header popup.
- Data uji: tanpa data yang dibuat atau diubah; spec hanya membaca.
- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1096: Kolom Role, Popup Role Count, Filter, dan Search untuk user Group Manager: baris pola dihitung sebagai penugasan aktif biasa tanpa badge

1. Ketik Search `Oscar`, tekan Enter
2. Verifikasi baris Oscar Pranata tampil di tabel
3. Verifikasi kolom Role Oscar Pranata berupa link berformat `N roles` dan bukan `0 roles`
4. Verifikasi kolom Role Oscar Pranata tanpa badge atau label Group Manager
5. Ganti isi kotak search dengan `Qori`, tekan Enter
6. Verifikasi baris Qori Akbar tampil di tabel
7. Verifikasi kolom Role Qori Akbar berupa link berformat `N roles` dan bukan `0 roles`
8. Verifikasi kolom Role Qori Akbar tanpa badge atau label Group Manager
9. Ganti isi kotak search dengan `Oscar`, tekan Enter
10. Klik label jumlah Role Oscar Pranata
11. Verifikasi header popup Role Count `Active Roles (N)` dengan N sama dengan angka pada label jumlah Oscar Pranata
12. Verifikasi popup memuat seksi Group Role dari baris pola
13. Verifikasi popup memuat seksi Transaction Role dari baris pola
14. Verifikasi popup tanpa bullet atau seksi Group Manager
15. Klik `[✕]` untuk menutup popup
16. Klik `(←)` pada kotak Search
17. Buka Filter Role, centang `Manage files`, klik `[Apply]`
18. Telusuri seluruh halaman Pagination tabel hingga Oscar Pranata dan Qori Akbar teramati
19. Verifikasi hasil Filter Role `Manage files` menyisakan antara lain Oscar Pranata
20. Verifikasi hasil Filter Role `Manage files` menyisakan antara lain Qori Akbar
21. Buka Filter Role, ganti pilihan menjadi `Approver`, klik `[Apply]`
22. Verifikasi hasil Filter Role `Approver` menyisakan `Eka Wulandari`, `Lukman Hakim`, `Mira Anggraini`, `Oscar Pranata`, `Qori Akbar`, `Yuda Pratama`
23. Verifikasi hasil Filter Role `Approver` berjumlah 6 baris
24. Hapus Filter Role
25. Ketik Search `Group Manager`, tekan Enter
26. Verifikasi empty state `No results found` tampil
27. Verifikasi Oscar Pranata tidak tampil di hasil Search `Group Manager`
28. Verifikasi Qori Akbar tidak tampil di hasil Search `Group Manager`
29. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 5, 9, 15, 16, 18, 24 dan 29. Search pada langkah 1, 5, 9 dan 25 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 5 sampai 8 menambah Search `Qori` karena Search `Oscar` pada TC langkah 1 tidak menampilkan Qori Akbar sementara Expected butir a memuatnya (lihat Temuan untuk QA). Langkah 18 menelusuri halaman agar baris target hasil Filter teramati (R-22). Langkah 15, 16 dan 29 membersihkan popup dan Search (S-09).
- Asersi tambahan atas Expected (S-03): langkah 2 dan 6 (baris target tampil) adalah anchor positif untuk asersi "tanpa badge" (langkah 4, 8); langkah 26 (`No results found`) adalah anchor positif yang sah untuk asersi absence hasil Search (8b butir 2) dan tidak ada di Expected TC.
- Angka Role (`48 roles` Oscar Pranata, `25 roles` Qori Akbar, formula `6 × 2 + 2 × 9 × 2`) tidak diasersi eksak (langkah 3, 7, 11) karena hitungan pola menunggu keputusan PM (PRD Open Item 3); asersi memakai bentuk `N roles` dan kesamaan label dengan header popup.
- Spec membaca saja; tidak ada state yang diubah.
- Temuan untuk QA:
  - TC-FA-SU-1096 mengacu Pre-setup #9 (Oscar Pranata, Group Manager IT Infrastructure dan Accounts Payable; `48 roles`), sedangkan Pre-setup #48 mendefinisikan Oscar Pranata sebagai Group Manager IT Infrastructure, Accounts Payable, dan Finance & Accounting; jumlah Role dan isi popup berbeda antar varian. Mohon dikonfirmasi varian yang berlaku untuk TC ini.
  - TC-FA-SU-1096 Expected butir a menyebut angka turunan `48 roles` dan `25 roles` yang bergantung perilaku hitung saat ini (PRD Open Item 3 belum diputuskan PM); spec tidak mengasersi angka eksak.
  - TC-FA-SU-1096 langkah 1 hanya Search `Oscar`, sedangkan Expected butir a juga mengasersi Qori Akbar; spec menambah Search `Qori` sebagai langkah penghubung (langkah 5).
  - TC-FA-SU-1096 Expected butir c menyebut hasil Filter Role `Approver` hanya enam pengguna, sedangkan Pre-setup #23 menyebut Lina Marlina (Total Control) memegang baris pola Transaction Role Approver pada setiap Jenis Transaksi × Group; spec mengikuti TC (enam baris, langkah 22 dan 23).
  - TC-FA-SU-1096 Expected butir d ("Search `Group Manager` tidak mencocokkan Oscar Pranata atau Qori Akbar") tidak menyebut hasil yang tampil; spec mengasersi empty state `No results found` sebagai anchor (langkah 26) dan mengandaikan tidak ada pengguna lain yang cocok.
  - TC-FA-SU-1096 langkah 3 ("hapus Search") dan langkah 5 ("Hapus Filter") tidak menyebut kontrol yang dipakai; spec memakai `(←)` pada kotak Search (8b butir 9) dan menghapus Filter Role lewat panel Filter.
