---
id: TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload
title: "Edit User: [Clear Field], Backdrop, Reload, Dialog Unsaved Changes (Cancel dan Leave), serta Penutupan Popup Tanpa Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-186
  - TC-GS-USER-187
  - TC-GS-USER-188
  - TC-GS-USER-189
  - TC-GS-USER-190
  - TC-GS-USER-191
  - TC-GS-USER-1007
  - TC-GS-USER-1063
coverage:
  web: automated
---

# Edit User: [Clear Field], Backdrop, Reload, Dialog Unsaved Changes (Cancel dan Leave), serta Penutupan Popup Tanpa Perubahan

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku Popup Edit User di browser.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Kebutuhan mock (Endpoint yang di-mock mengacu `global-settings/user/API/user-crud.yaml`: `POST /v2/iam/users/list` (daftar), `GET /v2/iam/users/{userId}` (detail untuk Popup Edit), `PATCH /v2/iam/users/{userId}` (Edit; tidak boleh terpanggil). Sumber opsi Position, Division, dan Access tidak ada di `user-crud.yaml`, ditentukan tim FE di tahap script; tidak ada endpoint yang dikarang):
  - Sesi dan payload izin akun Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan Access Level Total Control (Tabel Data Uji Pre-setup No. 2). Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons daftar User yang memuat baris Dewi Lestari: First Name `Dewi`, Last Name `Lestari`, Position `Staff`, Division `Finance`, Access `Fixed Asset` dan `Global Settings`.
  - Respons opsi Position (memuat `Staff` dan `Supervisor`), Division, dan produk Access yang dibutuhkan Popup Edit.
  - Request simpan Edit User tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC yang men-submit).
- Env var: `GS_TC_PASSWORD` (hanya dipakai run non-mock; didaftarkan di `executionConfig.environmentVariables`).
- Data: memakai baris Dewi Lestari dari respons mock; tidak ada data yang dibuat atau diubah, sehingga tidak ada seeding dan cleanup.
- Kemampuan teknis: klik area backdrop di luar Popup; memuat ulang halaman (F5) dengan dialog native `beforeunload` ditangani (dialog diamati lalu ditutup dengan memilih tetap di halaman); menekan Esc; mendeteksi muncul tidaknya dialog.
- State global yang diubah: tidak ada. Sesi sudah berada di akun default suite (Total Control), sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-USER-186: [Clear Field] mengosongkan seluruh field

1. Buka row action baris `Dewi Lestari` lalu klik `Edit`
2. Klik `[Clear Field]`
3. Verifikasi First Name kosong dan menampilkan placeholder
4. Verifikasi Last Name kosong dan menampilkan placeholder
5. Verifikasi Position kosong dan menampilkan placeholder
6. Verifikasi Division kosong dan menampilkan placeholder
7. Verifikasi Employee ID kosong dan menampilkan placeholder
8. Verifikasi Email kosong dan menampilkan placeholder
9. Verifikasi tidak ada dialog konfirmasi

### TC-GS-USER-1007: Klik backdrop saat form diubah tidak menutup Popup

10. Pilih Position `Supervisor`
11. Klik area backdrop
12. Verifikasi Popup Edit tetap terbuka
13. Verifikasi Position tetap `Supervisor`
14. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-USER-191: Reload halaman saat form dirty

15. Tekan F5
16. Verifikasi browser menampilkan dialog native konfirmasi meninggalkan halaman
17. Tutup dialog native dengan memilih tetap di halaman

### TC-GS-USER-190: Dialog Unsaved Changes, [Cancel] kembali ke form

18. Tekan `Esc`
19. Klik `[Cancel]`
20. Verifikasi Popup Edit tetap terbuka
21. Verifikasi Position tetap `Supervisor`

### TC-GS-USER-188: Tutup setelah mengubah field memunculkan dialog Unsaved Changes

22. Klik `[✕]`
23. Verifikasi dialog Title `Unsaved Changes`
24. Verifikasi body dialog `You have unsaved changes. Are you sure you want to leave?`
25. Verifikasi dialog memiliki tombol `[Cancel]` dan `[Leave]`

### TC-GS-USER-189: Dialog Unsaved Changes, [Leave] membuang perubahan

26. Klik `[Leave]`
27. Verifikasi Popup Edit tertutup
28. Verifikasi sel Position baris `Dewi Lestari` tetap `Staff`
29. Verifikasi data baris `Dewi Lestari` di tabel tidak berubah (butir "data tersimpan tidak berubah sampai Save" TC-GS-USER-186)

### TC-GS-USER-1063: Field diubah lalu dikembalikan, tutup Popup tanpa dialog

30. Buka row action baris `Dewi Lestari` lalu klik `Edit`
31. Ubah First Name `Dewi` menjadi `Dewa`
32. Ubah kembali First Name menjadi `Dewi`
33. Klik `[✕]`
34. Verifikasi Popup Edit langsung tertutup
35. Verifikasi dialog Unsaved Changes tidak muncul
36. Verifikasi data baris `Dewi Lestari` di User List tidak berubah

### TC-GS-USER-187: Tutup tanpa perubahan via [✕]

37. Buka row action baris `Dewi Lestari` lalu klik `Edit`
38. Klik `[✕]`
39. Verifikasi Popup Edit tertutup
40. Verifikasi dialog Unsaved Changes tidak muncul

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-186, 187, 188, 189, 190, 191, 1007, 1063). Mode: mock. Kelas harness: perilaku penutupan Popup Edit (satu kelas).
- Urutan TC di spec: 186, 1007, 191, 190, 188, 189, 1063, 187. Urutan sumber diubah menurut keadaan form (bagian 3 butir 6): pembukaan pertama memakai form yang sudah dikosongkan lewat `[Clear Field]` (tidak dihitung bersih) untuk TC-GS-USER-1007, 191, 190, 188, dan 189, yang semuanya membutuhkan form dirty; TC-GS-USER-189 menutup form lewat `[Leave]`. TC-GS-USER-1063 (dikembalikan ke nilai awal) dan TC-GS-USER-187 (tanpa perubahan) membutuhkan form baru dan berjalan terakhir dengan pembukaan masing-masing. Jumlah pembukaan form (tiga) sama dengan jumlah kejadian menutup form.
- Pada pembukaan pertama, Position `Supervisor` dipilih sesudah `[Clear Field]` (field kosong), sehingga form dirty; nilai ini sama dengan Data Uji TC-GS-USER-189 dan 190.
- TC-GS-USER-188 dan 189 berbagi dialog yang sama (`[✕]`, dialog, lalu `[Leave]`); TC-GS-USER-190 membuka dialog lewat `Esc` lalu `[Cancel]` sehingga form tetap dirty untuk TC-GS-USER-188.
- Langkah buka layar User List tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`; Precondition b). Langkah penghubung (aksi tanpa `Verifikasi` yang bukan langkah TC): langkah 17 (menutup dialog native dengan memilih tetap di halaman; kemampuan ini tertulis di Prerequisites, S-08).
- Butir "data tersimpan tidak berubah sampai Save" (TC-GS-USER-186 butir c) diasersi pada langkah 29 setelah form ditutup dengan `[Leave]`; pada mode mock ini berarti baris tabel tidak berubah.
- Pembagian TC lintas spec: TC-GS-USER-186 sampai 191, 1007, dan 1063 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-191 berstatus Automation `Manual Only`, bergantung pada dialog native `beforeunload`; spec memakai kemampuan menangani dialog native (diamati, lalu tetap di halaman) yang disediakan tim FE.
  - TC-GS-USER-186 butir a ("Semua field kosong") tidak merinci field mana saja (Access, avatar, Custom Field, TAG tidak disebut); spec mengasersi enam field teks dan dropdown Edit (First Name, Last Name, Position, Division, Employee ID, Email).
  - TC-GS-USER-186 butir c ("data tersimpan tidak berubah sampai Save") tidak menyebut cara memeriksa; spec memeriksa baris tabel setelah form ditutup.
  - TC-GS-USER-190 langkah 3 tidak menyebut bahwa `Esc` pada form dirty memunculkan dialog Unsaved Changes; spec mengikuti TC dan tidak mengasersi dialog tersebut sebelum `[Cancel]`.
- Spec melewati sekitar 35 langkah (40 langkah) karena memuat satu kelas (penutupan Popup Edit, mode mock), satu layar, tiga pembukaan form yang dipakai bersama sesuai keadaan dirty-nya, dan tiap blok TC berdiri sendiri.
