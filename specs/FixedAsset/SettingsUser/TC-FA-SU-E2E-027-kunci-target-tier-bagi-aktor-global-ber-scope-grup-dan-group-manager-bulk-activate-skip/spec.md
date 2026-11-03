---
id: TC-FA-SU-E2E-027-kunci-target-tier-bagi-aktor-global-ber-scope-grup-dan-group-manager-bulk-activate-skip
title: "Kunci Target Tier bagi Aktor Global, Ber-scope Grup, dan Group Manager: Sakelar OFF Disabled dan Bulk Activate Skip"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1065
coverage:
  web: automated
---

# Kunci Target Tier bagi Aktor Global, Ber-scope Grup, dan Group Manager: Sakelar OFF Disabled dan Bulk Activate Skip

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Lina Marlina, Pre-setup #1, akun default suite, `Spectra.env.FA_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control. Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Tabel "Pengguna dinonaktifkan" (langkah 1 sampai 4, precondition TC; dipakai sebagai precondition, tidak diasersi): Citra Lestari (Read Only), Gita Permata, Indra Wijaya.
- Tabel "Aktor" (satu blok per aktor karena ganti akun menuntut Step eksplisit; langkah 6 sampai 29 diulang per baris):

| Aktor | Pre-setup | Nama | Pengguna eligible (Bulk Activate) | Email | Env password |
|---|---|---|---|---|---|
| Manage global user & role (Update) | #4 | Qori Akbar | Doni Prasetyo | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Manage user & role Group (Update) | #6 | Sinta Dewi | Gita Permata | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
| Group Manager (IT Infrastructure dan Accounts Payable) | #9 | Oscar Pranata | Indra Wijaya | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_GM_PASSWORD` |

- Nama env `FA_MURG_UPD_PASSWORD`, `FA_MURGR_UPD_PASSWORD`, dan `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client `FaUserMain` (#20; Doni Prasetyo Inactive dengan Home Group Logistics Warehouse), pohon grup (#21), tier dan penugasan (#23). Citra Lestari, Gita Permata, Indra Wijaya, dan Doni Prasetyo adalah data Pre-setup yang diubah status aktifnya; keanggotaan scope tiap aktor ditetapkan Pre-setup #20 dan #23 sehingga data itu tidak dapat dimiliki spec. Semuanya dipulihkan ke status Pre-setup (Citra Lestari, Gita Permata, Indra Wijaya Active; Doni Prasetyo Inactive) lewat seed API pada langkah 30 dan hook `after`; efeknya (Last Updated dan entri audit trail) tidak dibalik.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen; seleksi baris berlanjut saat isi Search berganti (diasumsikan, lihat Temuan untuk QA); seed API untuk memulihkan status aktif; pembacaan jumlah entri Tab Changelog sebagai baseline (S-12) lewat UI.
- State global yang diubah: status aktif keempat pengguna di atas (dipulihkan pada langkah 30 dan hook `after`).

## Test Steps

### TC-FA-SU-1065: Activate target Read Only yang Inactive, sakelar OFF Disabled dan baris tier di-skip pada Bulk Activate

Untuk setiap pengguna pada tabel "Pengguna dinonaktifkan" di `## Prerequisites`, jalankan langkah 1 sampai 4.

1. Ketik Search nama pengguna, tekan Enter
2. Klik sakelar Active baris pengguna menjadi OFF
3. Klik `[Deactivate]` pada dialog konfirmasi
4. Klik `(←)` pada kotak Search
5. Tunggu aksi selesai (sakelar baris pengguna terakhir berstatus OFF)

Untuk setiap baris pada tabel "Aktor" di `## Prerequisites`, jalankan langkah 6 sampai 29.

6. Ganti akun: logout lalu login sebagai aktor baris tabel
7. Buka Settings > User dari sidebar
8. Ketik Search `Citra Lestari`, tekan Enter
9. Hover sakelar Active baris Citra Lestari (OFF)
10. Verifikasi sakelar Active baris Citra Lestari Disabled dengan tooltip `You don't have permission to edit.`
11. Buka Detail Citra Lestari lalu Tab Changelog
12. Catat jumlah entri Tab Changelog Citra Lestari sebagai baseline
13. Buka Settings > User dari sidebar
14. Ketik Search `Citra Lestari`, tekan Enter
15. Centang baris Citra Lestari
16. Verifikasi checkbox baris Citra Lestari tercentang
17. Ganti isi kotak search dengan nama pengguna eligible aktor, tekan Enter
18. Centang baris pengguna eligible
19. Klik Bulk Action > `[Activate]`
20. Verifikasi dialog campuran mencantumkan pengguna eligible pada kelompok `The following will be activated:`
21. Verifikasi dialog campuran mencantumkan Citra Lestari pada kelompok `The following will be skipped (already active, inactive in Global Settings, or no permission):`
22. Klik `[Continue]`
23. Verifikasi toast "Success, user has been activated. Some items were skipped."
24. Ganti isi kotak search dengan nama pengguna eligible aktor, tekan Enter
25. Verifikasi sakelar Active baris pengguna eligible ON (Active)
26. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
27. Verifikasi sakelar Active baris Citra Lestari tetap OFF (Inactive)
28. Buka Detail Citra Lestari lalu Tab Changelog
29. Verifikasi jumlah entri Tab Changelog Citra Lestari sama dengan baseline langkah 12 (tidak ada entri `Activate`)

30. Pulihkan Citra Lestari, Gita Permata, dan Indra Wijaya menjadi Active serta Doni Prasetyo menjadi Inactive lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Spec berisi satu TC dengan tiga aktor; ditulis per baris tabel "Aktor" karena langkah tiap aktor identik tetapi ganti akun menuntut Step eksplisit (akun pertama di hook `before` adalah Total Control untuk langkah precondition). Aksi Bulk Activate ada di tengah blok dan pemulihan pada langkah 30 (S-10).
- Spec melewati sekitar 35 langkah (30 langkah nominal, 86 langkah dengan ekspansi). Alasan: satu TC (satu kelas, fungsional kunci target tier) yang tiga aktornya memakai langkah identik (satu TC satu spec). Langkah yang diulang: langkah 1 sampai 4 untuk tiga pengguna (+8) dan langkah 6 sampai 29 untuk tiga aktor (+48); parameter ada di tabel `## Prerequisites`.
- Langkah 1 sampai 4 dan 5 memenuhi precondition langkah 1 TC (Total Control menonaktifkan Citra Lestari, Gita Permata, dan Indra Wijaya); Expected tidak mengasersinya, sehingga tidak ada `Verifikasi`. Langkah 5 adalah langkah penghubung "Tunggu aksi selesai" karena langkah berikutnya mengganti akun (bagian 8b butir 8).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris target pada langkah 1, 8, 14, 17, 24, 26 dan menutupnya pada langkah 4 (R-16); langkah 7 dan 13 (membuka Settings > User); langkah 30 (pemulihan state, S-09).
- Asersi "tidak menulis entri `Activate`" Expected c dikerjakan di spec ini sebagai selisih jumlah entri terhadap baseline (langkah 12 dan 29), bukan asersi absence kelas g (bagian 3 prinsip 13g: asersi jumlah dengan baseline boleh di spec fungsional). Baseline langkah 12 adalah anchor positif untuk langkah 29 (bagian 8b butir 2). Langkah 23 (toast sukses) menandai respons server selesai sebelum langkah 25 dan 27.
- Temuan untuk QA:
  - TC-FA-SU-1065 Expected c ("tidak menulis entri `Activate`") tidak menyebut surface log; spec mengamati Tab Changelog Citra Lestari saja. Penulisan log bersifat eventual (NC-03), sehingga selisih nol pada langkah 29 dapat lolos sebelum entri tertulis; usulan QA: tambahkan batas tunggu atau spec absence untuk TC ini.
  - TC-FA-SU-1065 langkah 1 menyebut "sakelar baris lalu `[Deactivate]`" tanpa menyebut dialog; spec memakai tombol `[Deactivate]` pada dialog konfirmasi sesuai teks TC. TC-FA-SU-1065 langkah 3 mencentang dua pengguna sekaligus tanpa menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti.
  - Doni Prasetyo (Inactive pada Pre-setup #20) adalah pengguna eligible aktor Qori Akbar dan diaktifkan oleh spec; status awalnya dipulihkan pada langkah 30.
  - Email akun #4, #6, dan #9 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
