---
id: TC-FA-SU-E2E-062-tambah-lalu-hapus-sebelum-save-save-dengan-0-grup-dan-clear-field
title: "Tambah Lalu Hapus Sebelum Save, Save dengan 0 Grup, dan Clear Field"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-204
  - TC-FA-SU-205
  - TC-FA-SU-206
coverage:
  web: automated
---

# Tambah Lalu Hapus Sebelum Save, Save dengan 0 Grup, dan Clear Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Wawan Setiawan; Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya (2 grup). Hook `before` menyetel Delete Branch Surabaya tercentang lewat seed API karena TC-FA-SU-204 menyebut "Branch Surabaya (D tercentang tersimpan)" (lihat Temuan untuk QA); Role Count awal Wawan 7 roles (Pre-setup #43).
- Data uji: grup Branch Surabaya dihapus dan ditambahkan kembali sebelum Save (TC-FA-SU-204); seluruh 2 grup `Manage files` dilepas (TC-FA-SU-205 dan 206).
- Kemampuan teknis: seed API untuk menyetel dan memulihkan penugasan Group Role `Manage files` Wawan Setiawan (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: penugasan Group Role `Manage files` milik Wawan Setiawan dan Role Count-nya; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-204: Menambah lalu menghapus grup yang sama sebelum Save: pemulihan nilai C/R/U/D tersimpan dan Save no-op

1. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
2. Buka popup Assign Group Role Manage files
3. Hapus Branch Surabaya dari tabel popup
4. Klik `[+ Assign Group]` untuk membuka popup Select Group
5. Verifikasi node Branch Surabaya dapat dipilih (tidak Disabled)
6. Centang Branch Surabaya lalu klik `[Select]`
7. Verifikasi baris Branch Surabaya kembali dengan nilai Delete tersimpan tercentang (bukan unchecked)
8. Klik `[Save]`
9. Verifikasi toast "No changes to save."

### TC-FA-SU-205: Save dengan 0 grup melepas seluruh penugasan: role tampil tanpa grup, tidak aktif, dan log Remove per grup

10. Catat Role Count Wawan Setiawan di User List dan jumlah entri `Remove` Object `Group Role` Wawan Setiawan pada Tab Changelog sebagai baseline
11. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
12. Klik `[Clear Field]`
13. Klik `[Save]`
14. Verifikasi tidak ada dialog konfirmasi tambahan (target bukan Group Manager)
15. Verifikasi toast "Success, group role has been updated."
16. Verifikasi kolom Group baris Manage files menjadi `—`
17. Verifikasi role Manage files tidak aktif
18. Buka User List
19. Verifikasi Role Count Wawan Setiawan berkurang dibanding baseline
20. Buka Tab Changelog, Search `Wawan Setiawan`, tekan Enter, lalu muat ulang sampai entri tampil
21. Verifikasi dua entri `Remove` / Object `Group Role` untuk IT Infrastructure dan Branch Surabaya (Old Value `Assigned` / New Value `—`) bertambah dibanding baseline pada Tab Changelog
22. Verifikasi tidak ada entri role-level tambahan: total entri baru pada Tab Changelog tepat dua

### TC-FA-SU-206: Clear Field mengosongkan baris tanpa menutup popup dan tanpa menyimpan

23. Pulihkan penugasan Manage files Wawan Setiawan (IT Infrastructure dan Branch Surabaya) lewat seed API
24. Buka ulang Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage files
25. Klik `[Clear Field]`
26. Verifikasi seluruh baris grup dan centang dikosongkan
27. Verifikasi popup tetap terbuka
28. Verifikasi empty state `No groups assigned yet`
29. Klik `[✕]`
30. Verifikasi dialog `Unsaved Changes`
31. Klik `[Leave]`
32. Buka ulang popup Assign Group Role Manage files
33. Verifikasi penugasan tersimpan tidak berubah: baris IT Infrastructure dan Branch Surabaya masih tampil
34. Klik `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 10, 23 dan 34. Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan penugasan sebelum TC berikutnya mengandalkannya (S-09); penutupan popup dirty mengikuti S-08.
- Langkah pola baca-log: langkah 20 sampai 22. Search `Wawan Setiawan` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- TC-FA-SU-205: asersi "tidak ada dialog konfirmasi tambahan" ditulis segera setelah `[Save]` dan sebelum toast sukses yang menjadi bukti respons sudah diproses (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-FA-SU-204 menyebut "Branch Surabaya (D tercentang tersimpan)" sedangkan TC-FA-SU-194 menyebut Delete Branch Surabaya tidak tercentang pada `Manage files` yang sama dan TC-FA-SU-201 mengubahnya dari Inactive ke Active; spec ini menyetel Delete tercentang lewat seed API sebagai precondition TC-FA-SU-204 dan tidak menyentuh asumsi TC lain.
  - TC-FA-SU-205 butir b ("Role Count berkurang") dan butir a ("tanpa dialog tambahan") tidak menyebut cara observasi selain User List dan toast; spec mengasersi sesuai teks TC.
  - Post Condition TC-FA-SU-204 sampai 206 (penugasan tersimpan tidak berubah, tidak ada entri log baru) tidak punya langkah observasi di TC dan tidak diasersi; pada TC-FA-SU-205 Post Condition butir c (Settings > Role & Permission) juga tidak diasersi.
