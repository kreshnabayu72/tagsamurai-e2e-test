---
id: TC-GS-USER-E2E-039-edit-tambah-access-dan-produk-kehilangan-subscription
title: "Edit User: Tambah Access Produk Baru Tanpa Dialog dan Produk Kehilangan Subscription"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-196
  - TC-GS-USER-197
coverage:
  web: automated
---

# Edit User: Tambah Access Produk Baru Tanpa Dialog dan Produk Kehilangan Subscription

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup yang dipakai: Client PT Maju Bersama dengan subscription `Fixed Asset` dan `Supply Asset` (No. 26), Position `Staff` (No. 22), Division `Finance` (No. 23); hanya dibaca. Spec tidak mengubah data user Pre-setup (Dewi Lestari No. 12 dan Joko Susilo No. 19 diganti user seed milik spec, S-06).
- Data Dinamis, di-seed lewat API di hook `before` selagi subscription `Supply Asset` Client aktif (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user: Position `Staff`, Division `Finance`:
  - U-D1 (TC-GS-USER-196): Name `Dewi Lestari {runId}-039`, Email `dewilestari+{runId}-039@qwertysystem.net`, Access `Fixed Asset` dan `Global Settings` (tanpa `Supply Asset`).
  - U-J (TC-GS-USER-197 butir a): Name `Joko Susilo {runId}-039`, Email `jokosusilo+{runId}-039@qwertysystem.net`, Access `Fixed Asset` dan `Supply Asset`.
  - U-D2 (TC-GS-USER-197 butir b): Name `Dewi Anggraini {runId}-039`, Email `dewianggraini+{runId}-039@qwertysystem.net`, Access `Fixed Asset` dan `Global Settings` (tanpa `Supply Asset`). User terpisah dari U-D1 karena U-D1 sudah memiliki `Supply Asset` setelah TC-GS-USER-196.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-D1, U-J, dan U-D2 lewat API.
- State global yang diubah: subscription `Supply Asset` Client dicabut di langkah 8 (aksi langsung ke server) dan dipulihkan di hook `after` walau spec gagal di tengah. Kemampuan mencabut dan memulihkan subscription disediakan tim FE/BE (TC tidak memberi cara; endpoint tidak disebut di TC dan PRD). Spec ini mengubah subscription Client default suite, sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`); spec lain tidak berjalan bersamaan.
- Kemampuan teknis: mencabut dan memulihkan subscription produk Client (lihat di atas); membaca opsi Access di Popup Edit, termasuk keadaan terpilih dan enabled.

## Test Steps

### TC-GS-USER-196: Tambah Access produk baru tidak memicu dialog

1. Klik icon Search, ketik `Dewi Lestari {runId}-039`, tekan Enter
2. Buka row action baris `Dewi Lestari {runId}-039` lalu klik `Edit`
3. Pilih Access `Supply Asset`
4. Klik `[Save]`
5. Verifikasi toast sukses: `Success, user has been updated.`
6. Verifikasi tidak ada dialog
7. Verifikasi sel Access baris `Dewi Lestari {runId}-039` memuat `Supply Asset`

### Pencabutan subscription

8. Cabut subscription `Supply Asset` Client (aksi langsung ke server, disediakan tim FE/BE)
9. Muat ulang halaman (F5)

### TC-GS-USER-197: Produk yang kehilangan subscription

10. Klik icon Search, ketik `Joko Susilo {runId}-039`, tekan Enter
11. Buka row action baris `Joko Susilo {runId}-039` lalu klik `Edit`
12. Verifikasi Access `Supply Asset` tampil terpilih
13. Hapus pilihan Access `Supply Asset`
14. Verifikasi Access `Supply Asset` tidak lagi terpilih (pilihan bisa dihapus)
15. Klik `[✕]`
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik `[Leave]`
18. Ganti isi kotak search dengan `Dewi Anggraini {runId}-039`, tekan Enter
19. Buka row action baris `Dewi Anggraini {runId}-039` lalu klik `Edit`
20. Verifikasi opsi Access `Fixed Asset` dan `Global Settings` tampil
21. Verifikasi opsi `Supply Asset` tidak tampil (tidak bisa ditambahkan baru)
22. Tekan `Esc`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-196, 197). Mode FE+BE; kelas harness: Edit Access terhadap subscription Client (satu kelas).
- Urutan TC di spec: 196, pencabutan subscription, 197, sama dengan urutan sumber. TC-GS-USER-196 membutuhkan subscription `Supply Asset` aktif sedangkan TC-GS-USER-197 membutuhkan subscription tidak aktif pada Client yang sama, sehingga subscription dicabut di tengah spec (langkah 8) dan aksi yang mengubah state ini ditaruh sesudah TC yang membutuhkan keadaan normal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (membuka form), 8 dan 9 (pencabutan subscription dan muat ulang), 10 dan 11, 18 dan 19, 22 (menutup form bersih lewat `Esc`). Langkah 13 sampai 17 menguji "bisa di-uncheck" lewat penghapusan pilihan Access nyata lalu menutup form dirty secara deterministik (`[✕]`, `Unsaved Changes`, `[Leave]`, S-08); `Verifikasi` dialog (langkah 16) adalah asersi tambahan penutupan yang tidak ada di Expected TC.
- Asersi absence `Supply Asset` (langkah 21) didahului `Verifikasi` opsi pembanding pada surface yang sama (langkah 20) sesuai bagian 8b butir 2.
- Pembagian TC lintas spec: TC-GS-USER-196 dan 197 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-196 Post Condition ("Terdampak: Supply Asset > Settings > User (user muncul)") tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-USER-197 tidak menyebut cara membuat keadaan "subscription Supply Asset Client sudah tidak aktif"; kemampuan disediakan tim FE/BE. Precondition TC-GS-USER-196 (subscription aktif) dan TC-GS-USER-197 (tidak aktif) bertentangan bila dibaca untuk satu Client; spec menyusunnya berurutan dengan pencabutan di tengah.
  - TC-GS-USER-197 butir a ("bisa di-uncheck"; TC memakai istilah ini untuk penghapusan pilihan Access) tidak menyebut cara membuktikan; spec menghapus pilihan Access dan memeriksa keadaan tidak lagi terpilih.
  - TC-GS-USER-197 langkah 3 memakai Dewi Lestari tanpa menyebut bahwa user itu belum memiliki `Supply Asset`; spec memakai U-D2 yang tidak memiliki `Supply Asset`.
