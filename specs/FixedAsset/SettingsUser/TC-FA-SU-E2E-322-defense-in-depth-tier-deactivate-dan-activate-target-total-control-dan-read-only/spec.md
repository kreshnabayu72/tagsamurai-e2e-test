---
id: TC-FA-SU-E2E-322-defense-in-depth-tier-deactivate-dan-activate-target-total-control-dan-read-only
title: "Defense-in-depth Tier: Deactivate dan Activate Target Total Control dan Read Only (Tunggal dan Bulk) serta Assign Group Role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1064
  - TC-FA-SU-1066
  - TC-FA-SU-1067
coverage:
  web: automated
---

# Defense-in-depth Tier: Deactivate dan Activate Target Total Control dan Read Only (Tunggal dan Bulk) serta Assign Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 11 Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Lina Marlina (Total Control), Citra Lestari (Read Only), Doni Prasetyo, Gita Permata, Indra Wijaya. Pengguna eligible per aktor: Gita Permata (Sinta Dewi) dan Indra Wijaya (Oscar Pranata) pada TC-FA-SU-1064; Doni Prasetyo (Qori Akbar), Gita Permata (Sinta Dewi), Indra Wijaya (Oscar Pranata) pada TC-FA-SU-1066.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE. Jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum dan sesudah permintaan (baseline, S-12).
- Ganti akun pada spec ini hanya mengambil token sesi API aktor untuk klien HTTP (sesi UI tetap akun pertama). Akun aktor berikutnya pada TC-FA-SU-1066 dan 1067 dituliskan di tiap langkah ganti akun: Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`); Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`); Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`).
- State global dan pemulihan: Gita Permata dan Indra Wijaya berstatus Inactive sesudah TC-FA-SU-1064; Citra Lestari dinonaktifkan seed API pada langkah penghubung TC-FA-SU-1066; seluruh status pengguna dipulihkan ke Pre-setup #20 lewat seed API di hook `after`. Efek pada Pre-setup: Last Updated dan Modified By pengguna eligible berubah dan entri log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1064: Deactivate target Total Control dan Read Only: tunggal ditolak, bulk melewati target

1. Kirim permintaan langsung ke API Deactivate Lina Marlina memakai klien HTTP dengan token sesi Sinta Dewi
2. Verifikasi server menolak permintaan dengan status 403
3. Kirim permintaan langsung ke API Deactivate Citra Lestari memakai klien HTTP dengan token sesi Sinta Dewi
4. Verifikasi server menolak permintaan dengan status 403
5. Catat jumlah entri `Deactivate` pada Tab Changelog Lina Marlina, Citra Lestari, dan Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
6. Kirim permintaan langsung ke API bulk Deactivate berisi Lina Marlina, Citra Lestari, dan Gita Permata memakai klien HTTP dengan token sesi Sinta Dewi
7. Verifikasi item Lina Marlina dan Citra Lestari dilewati pada permintaan bulk
8. Verifikasi item eligible (Gita Permata) diproses (partial-success) dan berstatus Inactive (dibaca lewat API)
9. Verifikasi status Lina Marlina dan Citra Lestari tidak berubah (dibaca lewat API)
10. Verifikasi jumlah entri `Deactivate` bertambah satu hanya untuk Gita Permata dan sama dengan baseline untuk Lina Marlina dan Citra Lestari
11. Ganti akun: login API sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`) untuk klien HTTP
12. Kirim permintaan langsung ke API Deactivate Lina Marlina memakai klien HTTP dengan token sesi Oscar Pranata
13. Verifikasi server menolak permintaan dengan status 403
14. Kirim permintaan langsung ke API Deactivate Citra Lestari memakai klien HTTP dengan token sesi Oscar Pranata
15. Verifikasi server menolak permintaan dengan status 403
16. Catat jumlah entri `Deactivate` pada Tab Changelog Lina Marlina, Citra Lestari, dan Indra Wijaya, Tab System Log aktor, dan Activity Log sebagai baseline
17. Kirim permintaan langsung ke API bulk Deactivate berisi Lina Marlina, Citra Lestari, dan Indra Wijaya memakai klien HTTP dengan token sesi Oscar Pranata
18. Verifikasi item Lina Marlina dan Citra Lestari dilewati pada permintaan bulk
19. Verifikasi item eligible (Indra Wijaya) diproses (partial-success) dan berstatus Inactive (dibaca lewat API)
20. Verifikasi status Lina Marlina dan Citra Lestari tidak berubah (dibaca lewat API)
21. Verifikasi jumlah entri `Deactivate` bertambah satu hanya untuk Indra Wijaya dan sama dengan baseline untuk Lina Marlina dan Citra Lestari

### TC-FA-SU-1066: Activate target Read Only yang Inactive: tunggal ditolak, bulk melewati target

22. Nonaktifkan Citra Lestari lewat seed API sebagai precondition TC (Gita Permata, Indra Wijaya, dan Doni Prasetyo sudah Inactive)
23. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
24. Kirim permintaan langsung ke API Activate Citra Lestari (Read Only, Inactive) memakai klien HTTP dengan token sesi Qori Akbar
25. Verifikasi server menolak permintaan dengan status 403
26. Catat jumlah entri `Activate` pada Tab Changelog Citra Lestari dan Doni Prasetyo, Tab System Log aktor, dan Activity Log sebagai baseline
27. Kirim permintaan langsung ke API bulk Activate berisi Citra Lestari dan Doni Prasetyo memakai klien HTTP dengan token sesi Qori Akbar
28. Verifikasi item Citra Lestari dilewati pada permintaan bulk
29. Verifikasi item eligible (Doni Prasetyo) diproses (partial-success) dan berstatus Active (dibaca lewat API)
30. Verifikasi status Citra Lestari tetap Inactive (dibaca lewat API)
31. Verifikasi jumlah entri `Activate` bertambah satu hanya untuk Doni Prasetyo dan sama dengan baseline untuk Citra Lestari
32. Ganti akun: login API sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`) untuk klien HTTP
33. Kirim permintaan langsung ke API Activate Citra Lestari (Read Only, Inactive) memakai klien HTTP dengan token sesi Sinta Dewi
34. Verifikasi server menolak permintaan dengan status 403
35. Catat jumlah entri `Activate` pada Tab Changelog Citra Lestari dan Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
36. Kirim permintaan langsung ke API bulk Activate berisi Citra Lestari dan Gita Permata memakai klien HTTP dengan token sesi Sinta Dewi
37. Verifikasi item Citra Lestari dilewati pada permintaan bulk
38. Verifikasi item eligible (Gita Permata) diproses (partial-success) dan berstatus Active (dibaca lewat API)
39. Verifikasi status Citra Lestari tetap Inactive (dibaca lewat API)
40. Verifikasi jumlah entri `Activate` bertambah satu hanya untuk Gita Permata dan sama dengan baseline untuk Citra Lestari
41. Ganti akun: login API sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`) untuk klien HTTP
42. Kirim permintaan langsung ke API Activate Citra Lestari (Read Only, Inactive) memakai klien HTTP dengan token sesi Oscar Pranata
43. Verifikasi server menolak permintaan dengan status 403
44. Catat jumlah entri `Activate` pada Tab Changelog Citra Lestari dan Indra Wijaya, Tab System Log aktor, dan Activity Log sebagai baseline
45. Kirim permintaan langsung ke API bulk Activate berisi Citra Lestari dan Indra Wijaya memakai klien HTTP dengan token sesi Oscar Pranata
46. Verifikasi item Citra Lestari dilewati pada permintaan bulk
47. Verifikasi item eligible (Indra Wijaya) diproses (partial-success) dan berstatus Active (dibaca lewat API)
48. Verifikasi status Citra Lestari tetap Inactive (dibaca lewat API)
49. Verifikasi jumlah entri `Activate` bertambah satu hanya untuk Indra Wijaya dan sama dengan baseline untuk Citra Lestari
50. Nonaktifkan kembali Doni Prasetyo, Gita Permata, dan Indra Wijaya lewat seed API

### TC-FA-SU-1067: Permintaan langsung assign Group Role pada target Total Control dan Read Only

51. Ganti akun: login API sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`) untuk klien HTTP
52. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada Finance & Accounting untuk Lina Marlina memakai klien HTTP dengan token sesi Sinta Dewi
53. Verifikasi server menolak permintaan dengan status 403
54. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada Finance & Accounting untuk Citra Lestari memakai klien HTTP dengan token sesi Sinta Dewi
55. Verifikasi server menolak permintaan dengan status 403
56. Verifikasi penugasan Group Role Lina Marlina dan Citra Lestari tidak berubah dan tidak ada penugasan baru (dibaca lewat API)
57. Ganti akun: login API sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`) untuk klien HTTP
58. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada IT Infrastructure untuk Lina Marlina memakai klien HTTP dengan token sesi Oscar Pranata
59. Verifikasi server menolak permintaan dengan status 403
60. Kirim permintaan langsung ke API assign grup Group Role `Manage group` pada IT Infrastructure untuk Citra Lestari memakai klien HTTP dengan token sesi Oscar Pranata
61. Verifikasi server menolak permintaan dengan status 403
62. Verifikasi penugasan Group Role Lina Marlina dan Citra Lestari tidak berubah dan tidak ada penugasan baru (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-1064, 1066, dan 1067 berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: Expected 1064 dan 1066 tentang entri log berupa asersi jumlah dengan baseline (hanya item eligible menghasilkan entri; target tier tidak) dan tetap di spec ini (bagian 3, asersi jumlah bukan kelas g). Klausa "tidak ada entri log baru" TC-FA-SU-1067 diasersi di spec 337 (kelas g); id TC tetap di `sourceTc` kedua spec.
- Klausa tampilan Expected c TC-FA-SU-1064 dan 1066 (sakelar Disabled dengan tooltip "You don't have permission to edit.") tidak diasersi karena bagian 8b butir 1; diuji lewat jalur UI.
- TC-FA-SU-1066 Langkah Uji 1 (Total Control menonaktifkan Citra Lestari, Gita Permata, dan Indra Wijaya lewat sakelar baris) dijalankan lewat seeding API sebagai precondition (S-04); Gita Permata dan Indra Wijaya sudah Inactive dari TC-FA-SU-1064; ketiga pengguna eligible dinonaktifkan kembali sekali pada langkah 50.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 5, 16, 22, 26, 35, 44, 50.
- Ganti akun eksplisit (S-07): langkah 11, 23, 32, 41, 51, 57.
- Spec ini 62 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu kelas harness (defense-in-depth permintaan langsung, kelas a) dan satu topik (kunci tier target), tiap blok berdiri sendiri dan memakai pengguna eligible sendiri; ekspansi berasal dari TC sumber yang menuntut pengulangan untuk dua atau tiga aktor (Manage global user & role, Manage user & role Group, Group Manager).
- Temuan untuk QA:
  - Aktor TC-FA-SU-1064 dan 1067 mencakup Group Manager Oscar Pranata (#9) selain Sinta Dewi (#6); email dan password #4, #6, dan #9 tidak tertulis di Pre-setup TC (S-11, S-13).
  - Expected a TC-FA-SU-1064 menyebut status 403 hanya untuk permintaan tunggal; respons permintaan bulk (partial-success) tidak diberi kode status, sehingga spec mengasersi hasil per item.
  - Doni Prasetyo (Inactive pada Pre-setup #20) dipakai sebagai pengguna eligible TC-FA-SU-1066 untuk Qori Akbar; Gita Permata dan Indra Wijaya sudah Inactive sesudah TC-FA-SU-1064 dan dipakai sebagai precondition TC-FA-SU-1066, sehingga urutan blok TC-FA-SU-1064 sebelum TC-FA-SU-1066 dipertahankan.
