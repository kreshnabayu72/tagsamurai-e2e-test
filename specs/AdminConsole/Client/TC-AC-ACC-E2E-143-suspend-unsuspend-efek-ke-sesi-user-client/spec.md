---
id: TC-AC-ACC-E2E-143-suspend-unsuspend-efek-ke-sesi-user-client
title: "Suspend dan Unsuspend: Efek Read-only pada Sesi User Client di FAMS, Sesi Tidak Terputus, dan Override Dicabut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-192
  - TC-AC-ACC-644
  - TC-AC-ACC-960
coverage:
  web: automated
---

# Suspend dan Unsuspend: Efek Read-only pada Sesi User Client di FAMS, Sesi Tidak Terputus, dan Override Dicabut

## Prerequisites

- Mode: FE+BE.
- Konteks (kelas c, dua sesi paralel yang diasersi): Browser A (admin) dan Browser B (user Client) berjalan bersamaan pada TC-AC-ACC-644 dan 960; TC-AC-ACC-192 hanya memakai Browser B.
- Akun aktor Browser A: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi Browser A ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Akun Browser B (login lewat langkah eksplisit, ditutup di akhir tiap blok TC; S-09):

| Blok | Akun | Email | Env password | Client |
|---|---|---|---|---|
| TC-AC-ACC-192 | Client Default User A-LIF-3 | `clientDefaultUser_automated_ptSuspendTanpaProduk@qwertysystem.net` | `AC_CLIENT_LIF3_PASSWORD` | C-LIF-12 `PT Suspend Tanpa Produk` (Suspended, FAMS Active, Default User Activated; Residen, hanya dibaca) |
| TC-AC-ACC-644 | Client Default User A-16 | `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net` | `AC_CLIENT_DEFAULT_USER_PASSWORD` | C-01 `PT Sejahtera Abadi` (Active; di-Suspend lalu di-Unsuspend) |
| TC-AC-ACC-960 | Client Default User A-W3LIF-1 | `clientDefaultUser_automated_ptDitahanUjiCabut@qwertysystem.net` | `AC_CLIENT_W3LIF1_PASSWORD` | C-W3LIF-5 `PT Ditahan Uji Cabut` (Suspended, FAMS Active, Default User Activated; Unsuspend lalu Suspend kembali) |

- Kemampuan teknis: produk FAMS dapat diakses oleh user Client dengan sesi aktif; form tambah aset FAMS (field wajib selain Asset Name berisi nilai valid sembarang karena form dimiliki modul FAMS); menghapus aset uji "Aset Uji Cabut 01 {runId}-143" dan "Aset Uji Cabut 02 {runId}-143" di FAMS lewat fixture (disediakan tim FE/BE); hook `after` memanggil fixture itu bila aset masih ada (mis. spec gagal sebelum langkah 34), tanpa mengandaikan aset tersimpan.
- Data yang diubah lalu dipulihkan (S-06): `PT Sejahtera Abadi` (Suspend lalu Unsuspend) dan `PT Ditahan Uji Cabut` (Unsuspend lalu Suspend). Efek: baris Changelog dan Last Updated bertambah.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-192: Setelah Suspend, user Client login tetap bisa tetapi hanya read-only

1. [Browser B] Login sebagai Client Default User A-LIF-3 dan buka produk FAMS
2. [Browser B] Verifikasi login berhasil dan data aset FAMS tampil
3. [Browser B] Lihat daftar aset FAMS dan catat jumlah aset (J1)
4. [Browser B] Klik aksi tambah aset di FAMS dan simpan satu aset baru dengan Asset Name `Aset Uji Suspend 192`
5. [Browser B] Lihat daftar aset FAMS
6. [Browser B] Verifikasi aset baru tidak tersimpan (jumlah aset sama dengan J1)
7. [Browser B] Verifikasi user Client tidak dapat menulis data (read-only)
8. [Browser B] Tutup jendela Browser B dan hapus sesi login-nya

### TC-AC-ACC-644: Suspend tidak memutus sesi user Client yang sedang aktif

9. [Browser B] Login sebagai Client Default User A-16 dan buka halaman FAMS
10. [Browser B] Lihat data aset
11. [Browser A] Ketik Search `PT Sejahtera Abadi`, tekan Enter
12. [Browser A] Klik `[⋯]` pada baris `PT Sejahtera Abadi` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog
13. [Browser A] Tunggu aksi selesai (toast sukses "Success, client has been suspended." tampil)
14. [Browser B] Tanpa logout, muat ulang halaman FAMS
15. [Browser B] Verifikasi halaman FAMS termuat ulang tanpa dialihkan ke halaman Login
16. [Browser B] Verifikasi data aset tetap tampil
17. [Browser B] Coba menambah atau mengubah data aset
18. [Browser B] Verifikasi aksi tambah/ubah data tidak dapat dilakukan (read-only)
19. [Browser B] Tutup jendela Browser B dan hapus sesi login-nya
20. [Browser A] Klik sub-tab Suspended, ketik Search `PT Sejahtera Abadi`, tekan Enter, klik `[⋯]` pada baris `PT Sejahtera Abadi` → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

### TC-AC-ACC-960: Unsuspend mencabut override read-only: user Client dapat menulis lagi di FAMS tanpa login ulang

21. [Browser B] Login sebagai Client Default User A-W3LIF-1 dan buka halaman FAMS
22. [Browser B] Catat jumlah aset (J1)
23. [Browser B] Tambah satu aset baru dengan Asset Name `Aset Uji Cabut 01 {runId}-143` lalu simpan, dan lihat daftar aset
24. [Browser B] Verifikasi aset baru tidak tersimpan (jumlah aset tetap J1)
25. [Browser B] Verifikasi user Client tidak dapat menulis (read-only)
26. [Browser A] Klik sub-tab Suspended, ketik Search `PT Ditahan Uji Cabut`, tekan Enter
27. [Browser A] Klik `[⋯]` pada baris `PT Ditahan Uji Cabut` → pilih `Unsuspend` lalu klik `[Unsuspend]` pada dialog
28. [Browser A] Verifikasi toast sukses "Success, client has been unsuspended."
29. [Browser B] Tanpa logout, muat ulang halaman FAMS
30. [Browser B] Verifikasi halaman FAMS termuat ulang
31. [Browser B] Tambah satu aset baru dengan Asset Name `Aset Uji Cabut 02 {runId}-143` lalu simpan, dan lihat daftar aset
32. [Browser B] Verifikasi aset baru tersimpan (jumlah aset = J1 + 1)
33. [Browser B] Verifikasi user Client dapat menulis lagi sesuai level Total Control Default User
34. [Browser B] Hapus aset uji `Aset Uji Cabut 02 {runId}-143` di FAMS, lalu tutup jendela Browser B dan hapus sesi login-nya
35. [Browser A] Klik sub-tab Active, ketik Search `PT Ditahan Uji Cabut`, tekan Enter, klik `[⋯]` pada baris `PT Ditahan Uji Cabut` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Browser A]` dan `[Browser B]` menandai konteks.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas tiga TC satu jenis harness (dua sesi paralel admin dan user Client di FAMS); setiap blok memakai Client dan akun Browser B sendiri, dan Browser B ditutup di akhir blok (S-09), sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): "Tunggu aksi selesai" sebelum aksi sesi lain (langkah 13), penutupan Browser B dan pemulihan status (langkah 8, 19, 20, 34, 35; Post Condition TC-AC-ACC-644 dan 960), dan Search yang menemukan baris target (R-16).
- Nama data bersuffix (S-12): TC-AC-ACC-960 menulis nama aset literal `Aset Uji Cabut 01` dan `Aset Uji Cabut 02`; spec memakai `Aset Uji Cabut 01 {runId}-143` dan `Aset Uji Cabut 02 {runId}-143` agar sisa aset dari run yang gagal tidak bentrok.
- Post Condition TC-AC-ACC-192: `-`; TC-AC-ACC-644 ("Unsuspend PT Sejahtera Abadi") adalah langkah 20.
- Temuan untuk QA:
  - TC-AC-ACC-192 dan 644 memakai FAMS (modul lain) tanpa menyebut nilai field wajib pada form tambah aset; spec memakai Asset Name unik dan menyatakan field lain "nilai valid sembarang" (sama dengan TC-AC-ACC-960).
  - TC-AC-ACC-192 Precondition tidak menyebut Admin yang men-Suspend C-LIF-12 (sudah Suspended pada fixture); TC-AC-ACC-644 "sesi FAMS aktif" tidak menyebut cara membangun sesi selain login; spec memakai login Browser B.
  - Email dan password akun A-LIF-3, A-16, dan A-W3LIF-1 dirujuk dari Tabel A1/A3; nama env password baru (`AC_CLIENT_LIF3_PASSWORD`, `AC_CLIENT_DEFAULT_USER_PASSWORD`, `AC_CLIENT_W3LIF1_PASSWORD`) didaftarkan di tahap script.
