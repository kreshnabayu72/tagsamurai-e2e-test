---
id: TC-FA-SU-E2E-064-resilience-group-role-save-popup-assign-gagal-karena-server-error
title: "Resilience Group Role: Save Popup Assign Gagal karena Server Error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-211
coverage:
  web: automated
---

# Resilience Group Role: Save Popup Assign Gagal karena Server Error

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan; Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya.
- Data uji: respons Save popup Assign Group Role dipaksa 5xx; perubahan yang dicoba adalah mencentang Delete pada Branch Surabaya.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP Save popup Assign Group Role di atas backend nyata (kegagalan 5xx dipicu intercept, bagian 6 konvensi); intercept dilepas segera setelah pemicu selesai (S-09). Pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10).
- State global yang diubah: tidak ada penugasan yang tersimpan; perubahan popup dibuang lewat `[Leave]` dan intercept dilepas di hook `after` sebagai cadangan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-211: Save popup Assign Group Role gagal karena server error: popup tetap terbuka dan input dipertahankan

1. Catat jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline
2. Intercept respons Save popup Assign Group Role menjadi 5xx
3. Ketik Search `Wawan Setiawan`, tekan Enter, lalu buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
4. Buka popup Manage files dan centang Delete pada Branch Surabaya
5. Klik `[Save]`
6. Verifikasi toast "Error, failed to save group role."
7. Lepas intercept respons Save
8. Verifikasi popup tetap terbuka dengan input dipertahankan (Delete Branch Surabaya tercentang)
9. Verifikasi `[Save]` Enabled untuk retry
10. Klik `[✕]` pada popup yang masih terbuka
11. Verifikasi dialog `Unsaved Changes`
12. Klik `[Leave]`
13. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter
14. Verifikasi jumlah entri Object `Group Role` Wawan Setiawan pada Tab Changelog sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 7 dan 10 sampai 12. Intercept dilepas segera setelah toast error tampil (S-09); penutupan popup dirty mengikuti S-08; baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 13 dan 14. Search `Wawan Setiawan` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Klausa "tidak ada entri log" ditulis sebagai asersi jumlah dengan baseline pada aksi yang gagal (bagian 3 prinsip 13 butir g, S-12); toast error menjadi anchor positif.
- Langkah penghubung Search (S-03): Search nama pengguna target pada langkah 3 digabung ke langkah pembuka Detail atau pembacaan baris, untuk menemukan baris target di User List yang memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah berikutnya mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-FA-SU-211 tidak menyebut apakah popup yang tetap terbuka masih dirty setelah kegagalan; spec menutupnya lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
  - Post Condition TC-FA-SU-211 ("tidak ada perubahan tersimpan dan tidak ada entri baru") sudah tercakup oleh asersi jumlah entri log; perubahan tersimpan pada kolom Group tidak diasersi karena tidak ada langkah observasi di TC.
