---
id: TC-FA-SU-E2E-384-cancel-dialog-auto-revert-dari-popup-assign-group-role-popup-kembali-utuh
title: "Cancel Dialog Auto-Revert dari Popup Assign Group Role: Popup Kembali dengan Isi Utuh"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1079
coverage:
  web: automated
---

# Cancel Dialog Auto-Revert dari Popup Assign Group Role: Popup Kembali dengan Isi Utuh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Lina Marlina, Total Control (Pre-setup #1 dan #23), dan Citra Lestari, Read Only (Pre-setup #3 dan #23).
- Data uji: popup Assign Group Role `Manage files`; Lina Marlina: centang `Delete` pada `IT Infrastructure` dihapus lalu ikon hapus pada `Branch Surabaya`; Citra Lestari: ikon hapus pada `Branch Surabaya` (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (bagian 8b butir 10); seed API untuk memulihkan penugasan keduanya ke Pre-setup #23 bila perlu. Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik, batas 2 menit.
- State global yang diubah: tidak ada yang tersimpan (seluruh perubahan dibatalkan); penugasan Lina Marlina dan Citra Lestari tetap Pre-setup #23, dipulihkan lewat seed API di hook `after` sebagai jaring pengaman. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1079: Cancel dialog Auto-Revert D-05 dari popup Assign Group Role target Total Control atau Read Only: popup kembali dengan isi utuh dan tanpa penyimpanan

1. Catat jumlah entri Tab Changelog Lina Marlina dan Citra Lestari sebagai baseline
2. Ketik Search `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
3. Klik Tab Role lalu Sub-tab Group Role
4. Verifikasi banner `This user has Total Control access.` tampil
5. Buka popup Assign Group Role Manage files
6. Hapus centang Delete pada IT Infrastructure
7. Klik `[Save]`
8. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control` tampil
9. Klik `[Cancel]` pada dialog
10. Verifikasi dialog tertutup
11. Verifikasi popup Assign Group Role Manage files tampil kembali dengan centang Delete pada IT Infrastructure tetap tidak tercentang
12. Klik ikon hapus pada Branch Surabaya
13. Klik `[Save]`
14. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control` tampil
15. Klik `[Cancel]` pada dialog
16. Verifikasi dialog tertutup
17. Verifikasi popup tampil kembali dengan Branch Surabaya tetap terhapus dari popup
18. Klik `[✕]` untuk menutup popup
19. Verifikasi dialog Unsaved Changes tampil
20. Klik `[Leave]`
21. Verifikasi popup tertutup
22. Buka popup Assign Group Role Manage files
23. Verifikasi centang Delete pada IT Infrastructure tercentang
24. Verifikasi Branch Surabaya ada
25. Klik `[✕]` untuk menutup popup
26. Verifikasi banner `This user has Total Control access.` tetap tampil
27. Verifikasi baris Group Role dan role lain milik Lina Marlina tidak berubah
28. Buka Tab Changelog, Search `Lina Marlina`, tekan Enter, lalu muat ulang
29. Verifikasi jumlah entri Tab Changelog Lina Marlina sama dengan baseline
30. Kembali ke daftar User lewat Breadcrumb
31. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter, lalu klik Name `Citra Lestari`
32. Klik Tab Role lalu Sub-tab Group Role
33. Verifikasi banner `This user has Read Only access.` tampil
34. Buka popup Assign Group Role Manage files
35. Klik ikon hapus pada Branch Surabaya
36. Klik `[Save]`
37. Verifikasi dialog Auto-Revert D-05b dengan Title `Remove Read Only` tampil
38. Klik `[Cancel]` pada dialog
39. Verifikasi dialog tertutup
40. Verifikasi popup tampil kembali dengan Branch Surabaya tetap terhapus dari popup
41. Klik `[✕]` untuk menutup popup
42. Verifikasi dialog Unsaved Changes tampil
43. Klik `[Leave]`
44. Buka popup Assign Group Role Manage files
45. Verifikasi Branch Surabaya ada
46. Klik `[✕]` untuk menutup popup
47. Verifikasi banner `This user has Read Only access.` tetap tampil
48. Verifikasi baris Group Role dan role lain milik Citra Lestari tidak berubah
49. Buka Tab Changelog, Search `Citra Lestari`, tekan Enter, lalu muat ulang
50. Verifikasi jumlah entri Tab Changelog Citra Lestari sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 28, 30, 31, 49. Search pada langkah 2, 28, 31 dan 49 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12.
- Menutup popup dirty ditulis `[✕]`, dialog Unsaved Changes, `[Leave]` (S-08); penutupan popup bersih sesudah verifikasi memakai `[✕]` tanpa dialog.
- Alasan di atas sekitar 35 langkah (blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13, Smell): satu TC (satu spec per TC, C2) yang mencakup dua target berurutan (Lina Marlina lalu Citra Lestari) dan tiga skenario Cancel/Leave per target, tanpa kelas harness. Setiap Expected bermajemuk wajib satu `Verifikasi` per klausa (S-01), dan langkah tidak dapat dikurangi tanpa menghilangkan klausa Expected.
- Asersi "tidak ada entri log" dalam TC ditulis sebagai selisih nol terhadap baseline jumlah entri Tab Changelog (S-12), bukan asersi absence kelas g; Tab System Log aktor dan Activity Log tidak dibaca karena TC tidak menyebut surface log untuk skenario Cancel.
- TC-FA-SU-1078 (tambah grup yang menyimpangkan pola) ada di spec 379.
- Temuan untuk QA:
  - TC-FA-SU-1079 langkah 6 ("Ulangi langkah 2 sampai 3 pada Detail Citra Lestari") meminta menghapus centang Delete pada IT Infrastructure, padahal Citra Lestari (Read Only) hanya memegang Read sehingga Delete tidak tercentang dan tidak ada yang dihapus; spec memakai ikon hapus pada Branch Surabaya (langkah 4 TC) sebagai perubahan yang memicu dialog D-05b. Mohon dikonfirmasi perubahan yang dimaksud untuk Citra Lestari.
  - TC-FA-SU-1079 butir a menyebut "tidak ada request simpan" tanpa langkah observasi; spec membuktikannya lewat popup yang tetap dirty, nilai tersimpan semula setelah Leave, dan jumlah entri Tab Changelog yang sama dengan baseline.
  - Dialog D-05b untuk Citra Lestari tidak disebut TC pada langkah Cancel; spec mengasersi Title `Remove Read Only` mengikuti TC-FA-SU-1077.
