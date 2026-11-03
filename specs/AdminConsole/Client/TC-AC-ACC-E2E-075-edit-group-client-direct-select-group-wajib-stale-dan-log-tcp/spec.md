---
id: TC-AC-ACC-E2E-075-edit-group-client-direct-select-group-wajib-stale-dan-log-tcp
title: "Edit Client Direct: Select Group Terisi, Wajib, Group Dihapus Sebelum Save, dan Perubahan Group Tercatat (Total Control)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-137
  - TC-AC-ACC-538
  - TC-AC-ACC-539
  - TC-AC-ACC-540
coverage:
  web: automated
---

# Edit Client Direct: Select Group Terisi, Wajib, Group Dihapus Sebelum Save, dan Perubahan Group Tercatat (Total Control)

## Prerequisites

- Mode: FE+BE. Pelaku kedua (menghapus Group) memakai sesi API.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Dataset seed (nama bersuffix): Client `PT Baru Daftar {runId}-075` (replika C-09: Direct, Group Cabang Menteng, tanpa subscription, Default User Not Yet Activated `hadi.prasetyo+{runId}-075@qwertysystem.net`); Group sementara `Cabang Uji Hapus {runId}-075` di bawah Area Jakarta (dihapus pelaku kedua pada TC-539; hook `after` menghapus sisa). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Baseline (S-12): Search nama unik pada Changelog, System Log (Settings > User > Detail akun aktor > Tab System Log), dan Activity Log Admin Console memberi baseline nol sebelum TC-540.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-137 dan TC-538: Select Group terisi dan wajib

1. Ketik Search `PT Baru Daftar {runId}-075`, tekan Enter
2. Buka `⋯` baris `PT Baru Daftar {runId}-075` lalu klik `Edit`
3. Lihat Section Partner & Group
4. Verifikasi field Partner kosong dan read-only
5. Verifikasi field Select Group (tree-picker) tampil terisi "Cabang Menteng"
6. Klik `[Clear Field]`
7. Klik `[Save]`
8. Verifikasi pesan error di bawah Select Group: "Group must not be empty"
9. Verifikasi popup tetap terbuka
10. Verifikasi tidak ada toast
11. Klik `[✕]` di header popup
12. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
13. Klik `[Leave]`

### TC-539: Group dihapus sesi lain sebelum Save

14. Buka `⋯` baris `PT Baru Daftar {runId}-075` lalu klik `Edit`
15. Pilih Group "Cabang Uji Hapus {runId}-075" pada tree Select Group
16. Ubah Fax menjadi `0215550100`
17. Pelaku kedua (sesi API) menghapus Group "Cabang Uji Hapus {runId}-075" hingga terhapus
18. Tunggu aksi selesai
19. Klik `[Save]`
20. Verifikasi pesan error "This group no longer exists. Please select another."
21. Verifikasi pilihan Select Group dikosongkan dan opsi tree dimuat ulang tanpa "Cabang Uji Hapus {runId}-075"
22. Verifikasi Fax tetap "0215550100"
23. Verifikasi popup tetap terbuka
24. Klik `[✕]` di header popup
25. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
26. Klik `[Leave]`

### TC-540: Ubah Group tercatat di tiga log

27. Buka `⋯` baris `PT Baru Daftar {runId}-075` lalu klik `Edit`
28. Pilih Group "Area Jakarta" pada tree Select Group
29. Klik `[Save]`
30. Verifikasi popup tertutup
31. Verifikasi toast sukses "Success, client has been updated."
32. Verifikasi kolom Group baris "PT Baru Daftar {runId}-075" menampilkan "Area Jakarta"
33. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Baru Daftar {runId}-075`, tekan Enter
34. Verifikasi Changelog: Action `Edit`, Client Name "PT Baru Daftar {runId}-075", Field `Group`, Old Value `Cabang Menteng`, New Value `Area Jakarta`, Modified By aktor
35. Buka Settings > User > Detail akun aktor > Tab System Log, cari `PT Baru Daftar {runId}-075`
36. Verifikasi System Log: Action `Edit`, Object `Client`, Name "PT Baru Daftar {runId}-075", Field `Group`, Old Value `Cabang Menteng`, New Value `Area Jakarta`
37. Buka Activity Log Admin Console, cari `PT Baru Daftar {runId}-075`
38. Verifikasi Activity Log memuat baris yang sama dengan System Log, Modified By aktor

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 38 langkah): satu role dan satu Client seed; empat blok (screening dan wajib, stale, tulis dan log) berdiri sendiri, popup dibuka ulang karena `[Leave]` menutup form dirty.
- Pelaku kedua TC-539 memakai sesi API hingga Group terhapus (R-20); bukan konteks UI kedua. TC-539 bertanda Manual Only (dua sesi paralel) di TC.
- Langkah penghubung (S-03): `[Clear Field]` + `[Save]` pada TC-538 menguji wajib; penutup form dirty (S-08); Search nama unik; popup dibuka ulang sebelum tiap TC karena `[Leave]` menutup form dirty (jumlah buka sama dengan jumlah kejadian menutup).
- Temuan untuk QA:
  - TC-540 Post Condition ("Kembalikan Group ke Cabang Menteng lewat Edit") adalah pemulihan; cleanup menghapus Client seed lewat hook `after`.
