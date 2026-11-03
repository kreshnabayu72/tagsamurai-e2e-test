---
id: TC-AC-ACC-E2E-119-change-partner-kondisi-berubah-oleh-pelaku-lain
title: "Change Partner: Group Dihapus, Dialog Tidak Ter-refresh, dan Client Dihapus oleh Pelaku Lain Sebelum Confirm"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-188
  - TC-AC-ACC-627
  - TC-AC-ACC-638
coverage:
  web: automated
---

# Change Partner: Group Dihapus, Dialog Tidak Ter-refresh, dan Client Dihapus oleh Pelaku Lain Sebelum Confirm

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi UI yang diasersi): Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Pelaku kedua (hanya memicu perubahan state, memakai sesi API tanpa UI; bukan konteks kedua): untuk TC-AC-ACC-188 menghapus Group lewat API (setara Settings > Group) sebagai Total Control A-01; untuk TC-AC-ACC-627 menambah Partner sebagai Total Control A-01 (sesi API terpisah dari sesi UI); untuk TC-AC-ACC-638 menghapus Client sebagai Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (password `AC_CLIENT_ACTIVE_FULL_PASSWORD`). Sesi API aktor tidak dihitung sebagai sesi web (tidak mengusir sesi UI); kemampuan ini disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data: Group sementara `Cabang Uji Hapus {runId}-119` (di bawah Area Jakarta) dibuat lewat API di hook `before` dan dihapus oleh langkah TC-AC-ACC-188 (Tabel A3, kelas Sementara); hook `after` menghapus Group itu lewat API bila masih ada (mis. spec gagal sebelum langkah 5), tanpa mengandaikan seed berhasil penuh. Client C-13 `PT Ganti Mitra` literal tidak disentuh.
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Ganti Mitra {runId}-119` (setara C-13, Tabel A2: Active, hanya Partner CV Mitra Sejati, Group Area Jakarta, FAMS Active; relasinya tidak berubah pada spec ini karena `[Confirm]` gagal), `PT Ubah Mitra 15 {runId}-119` (setara C-ROL-8: Active, satu-satunya Partner CV Mitra Sejati, Group Area Jakarta, tanpa subscription; sesi pelaku kedua menambah "CV Mitra Lestari" lewat API) dan `PT Uji Konkurensi 04 {runId}-119` (setara C-LIF-22: Active, belum pernah memiliki subscription, relasi Partner hanya CV Mitra Sejati; dihapus oleh pelaku kedua, hook `after` menghapusnya bila masih ada). Client C-ROL-8 `PT Ubah Mitra 15` dan C-LIF-22 `PT Uji Konkurensi 04` literal tidak disentuh.
- Partner pembanding Active: `CV Mitra Lestari`.
- Jeda amat TC-AC-ACC-627: 30 detik nyata sesuai TC (TC menyatakan durasinya; konvensi bagian 6 menetapkan 5 detik hanya sampai TC menyatakan durasi).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-188: Select Group stale pada Change Partner Direct

1. Ketik Search `PT Ganti Mitra {runId}-119`, tekan Enter
2. Klik `[⋯]` pada baris `PT Ganti Mitra {runId}-119` → klik `Change Partner`
3. Klik `[Remove]` pada "CV Mitra Sejati"
4. Pilih Group "Cabang Uji Hapus {runId}-119" pada tree `Select Group*`
5. Hapus Group "Cabang Uji Hapus {runId}-119" lewat sesi API pelaku kedua hingga Group terhapus
6. Klik `[Confirm]`
7. Verifikasi pesan "This group no longer exists. Please select another."
8. Klik `[✕]` pada header dialog
9. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
10. Klik `[Leave]` pada dialog Unsaved Changes
11. Verifikasi dialog Change Partner tertutup
12. Verifikasi Managed By baris `PT Ganti Mitra {runId}-119` tetap "CV Mitra Sejati"

### TC-AC-ACC-627: Dialog Change Partner tidak ter-refresh oleh perubahan sesi lain sebelum Confirm

13. Ketik Search `PT Ubah Mitra 15 {runId}-119`, tekan Enter
14. Klik `[⋯]` pada baris `PT Ubah Mitra 15 {runId}-119` → klik `Change Partner` tanpa menekan `[Confirm]`
15. Tambah "CV Mitra Lestari" ke `PT Ubah Mitra 15 {runId}-119` lewat sesi API pelaku kedua hingga Partner tersimpan
16. Tunggu 30 detik tanpa aksi apa pun di dialog
17. Verifikasi dialog Change Partner tetap terbuka
18. Verifikasi list "Current Partners" hanya memuat "CV Mitra Sejati"
19. Verifikasi tidak ada dialog lain yang muncul
20. Verifikasi tidak ada toast
21. Klik `[✕]` pada header dialog

### TC-AC-ACC-638: Change Partner pada Client yang baru dihapus admin lain: toast netral dan kembali ke List

22. Ketik Search `PT Uji Konkurensi 04 {runId}-119`, tekan Enter
23. Klik `[⋯]` pada baris `PT Uji Konkurensi 04 {runId}-119` → klik `Change Partner`
24. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
25. Hapus Client `PT Uji Konkurensi 04 {runId}-119` (nama konfirmasi persis) lewat sesi API pelaku kedua Active-Full hingga Client terhapus
26. Klik `[Confirm]`
27. Verifikasi toast netral "This client is no longer available."
28. Verifikasi toast error "Error, failed to update partner." tidak tampil
29. Ketik Search `PT Uji Konkurensi 04 {runId}-119`, tekan Enter
30. Verifikasi List sub-tab Active disegarkan dan baris `PT Uji Konkurensi 04 {runId}-119` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pelaku kedua memakai sesi API (bukan UI) karena hasilnya di sesi itu tidak diasersi; sesuai konvensi bagian 3 prinsip 13 (P-2, keputusan 2026-10-30) tidak butuh butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20). TC asal menyebut sesi kedua UI dan "Manual Only (d) dua sesi paralel"; kebutuhan sesi UI ganda tidak ada karena sesi kedua tidak diasersi.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 8 dan 10 (`[✕]` dan `[Leave]` yang diminta TC-AC-ACC-188 langkah 7), langkah 21 (`[✕]` menutup dialog bersih; pemulihan Post Condition TC-AC-ACC-627 lewat API tidak dijalankan karena target adalah replika milik spec yang dibersihkan hook `after`), dan langkah 29 (Search ulang sesudah toast netral; toast netral sudah diasersi dan menjadi anchor absence baris, bagian 8b butir 2). Absence "toast error tidak tampil" (langkah 28) diletakkan segera setelah toast netral sebagai anchor positif (butir 11).
- Nama data bersuffix (S-12): TC-AC-ACC-188 menulis nama literal `Cabang Uji Hapus`; spec memakai `Cabang Uji Hapus {runId}-119` agar sisa Group dari run yang gagal tidak bentrok.
- Post Condition TC-AC-ACC-188 ("Group sudah terhapus; relasi tidak berubah"), TC-AC-ACC-638 (seed ulang; tidak diperlukan karena target adalah replika milik spec): tanpa langkah observasi di TC, tidak diasersi selain Expected.
- Temuan untuk QA:
  - TC-AC-ACC-627 Expected a "Dialog di sesi A tetap terbuka" hanya diamati selama 30 detik; TC tidak menyatakan apakah dialog tetap terbuka setelah itu.
  - TC-AC-ACC-188 langkah 5 menyebut "sesi lain lewat Settings > Group" tanpa akun pelaku; spec memakai Total Control A-01 lewat API ("disediakan tim FE" untuk kemampuan hapus Group).
