---
id: TC-AUTH-SES-E2E-025-client-suspended-dialog-access-restricted
title: "Client Suspended: Dialog Access Restricted, OK, dan Unsuspend"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-77
  - TC-AUTH-SES-78
  - TC-AUTH-SES-85
coverage:
  web: automated
---

# Client Suspended: Dialog Access Restricted, OK, dan Unsuspend

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend (Tabel Data Uji Pre-setup #32) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BASE milik Client Suspend (Tabel Data Uji Pre-setup #16, status Client Active di awal spec), Activated, Active ON, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-77: `Bayu Permata` (`bayupermata+{runId}-025@qwertysystem.net`)
  - TC-AUTH-SES-78: `Intan Lestari` (`intanlestari+{runId}-025@qwertysystem.net`)
  - TC-AUTH-SES-85: `Reza Saputra` (`rezasaputra+{runId}-025@qwertysystem.net`)
- Sesi uji (hook `before`, lewat login API; tiap user punya konteks Browser A sendiri): sesi platform web Active untuk ketiga user; sesi-produk Fixed Asset Active (seat terpakai) untuk Bayu Permata (TC-AUTH-SES-77).
- Akun aktor Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4, `Spectra.env.AC_PRINCIPAL_PASSWORD`) login di Browser Principal pada hook `before`; dipakai untuk Suspend dan Unsuspend Client Suspend. Browser Principal dan Browser A masing-masing user adalah konteks browser terpisah.
- Hook `after`: Unsuspend Client Suspend bila masih Suspended (pemulihan state tenant), akhiri semua sesi seed, logout Browser Principal dan kembalikan sesi ke akun default suite, hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Efek pada data Pre-setup bersama (S-06): Suspend dan Unsuspend Client Suspend (Tabel Data Uji Pre-setup #16, dipakai bersama spec lain) mengubah status Client dan Last Updated Client itu; status dikembalikan ke Active di akhir spec, Last Updated tidak dipulihkan.
- Kemampuan teknis (kelas harness h: state tenant): beberapa konteks browser bersamaan; event push SSE ke Browser A; pembacaan status sesi platform, sesi-produk, dan seat dari BE; halaman `Global Settings > User` dapat dibuka oleh `Intan Lestari` (TC-AUTH-SES-78); pengatur waktu server uji (Tabel Data Uji Pre-setup #18) yang dapat memajukan dan memulihkan jam server per menit, dengan jam browser/perangkat diatur bersama jam server (TC-AUTH-SES-85).
- Suite berjalan serial (`parallel: false`); state global yang diubah: status Client Suspend (Active menjadi Suspended pada TC-AUTH-SES-77, kembali Active pada TC-AUTH-SES-85) dan jam server serta jam browser/perangkat (diatur bersama pada TC-AUTH-SES-85), dipulihkan di hook `after`.
- Menunggu waktu nyata tidak dipakai; jeda 2 menit pada TC-AUTH-SES-85 dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama.

## Test Steps

### TC-AUTH-SES-77: Suspend Client memunculkan Dialog Access Restricted tanpa memutus sesi dan seat

1. Di Browser A (Intan Lestari) buka `Global Settings > User` dan ketik `Intan` pada form Search (halaman dengan form Search terisi, keadaan awal TC-AUTH-SES-78)
2. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Suspend
3. Di Browser A (Bayu Permata) amati layar → Dialog Access Restricted muncul
4. Verifikasi Dialog "Access Restricted" tampil dengan Body "Your organization's access has been suspended. You can still view data, but write actions are disabled until access is restored."
5. Verifikasi Dialog memuat satu tombol [OK]
6. Verifikasi Sesi platform `Bayu Permata` tetap Active
7. Verifikasi Sesi-produk Fixed Asset `Bayu Permata` tetap Active
8. Verifikasi Seat sesi-produk Fixed Asset `Bayu Permata` tidak dilepas

### TC-AUTH-SES-78: OK pada Dialog Access Restricted me-refresh halaman saat ini dan bukan logout

9. Di Browser A (Intan Lestari) amati layar → Dialog Access Restricted tampil pada halaman `Global Settings > User`
10. Di Browser A (Intan Lestari) klik [OK]
11. Verifikasi Halaman saat ini ter-refresh (`Global Settings > User`)
12. Verifikasi Data di-fetch ulang pada halaman yang sama (`Global Settings > User`)
13. Verifikasi Browser A tidak diarahkan ke halaman Login
14. Verifikasi Sesi tidak di-logout

### TC-AUTH-SES-85: Unsuspend Client tidak memunculkan dialog atau push simetris

15. Di Browser A (Reza Saputra) amati layar → Dialog Access Restricted tampil
16. Di Browser A (Reza Saputra) klik [OK] (dialog sudah ditutup sebelum Unsuspend)
17. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Unsuspend
18. Di Browser A (Reza Saputra) majukan jam server uji dan jam browser/perangkat bersama 2 menit sambil menggerakkan mouse, lalu amati layar
19. Verifikasi Tidak ada dialog atau toast apa pun di Browser A
20. Verifikasi Sesi `Reza Saputra` tetap Active
21. Di Browser A (Reza Saputra) refresh halaman atau navigasi ke halaman lain
22. Verifikasi App Access kembali ke level sebelumnya pada refresh atau navigasi berikutnya (aksi tulis tersedia kembali)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant: Client Suspended).
- Satu kali Suspend (langkah 2) memunculkan dialog di Browser A ketiga user sekaligus karena ketiganya milik Client Suspend; TC-AUTH-SES-78 dan TC-AUTH-SES-85 memakai dialog yang sudah tampil sebagai precondition-nya (S-04). Kondisi "Dialog sudah ditutup" TC-AUTH-SES-85 dipenuhi dengan klik [OK] pada langkah 16 (salinan langkah TC-AUTH-SES-78 yang menjadi dependensinya).
- Urutan mengikuti TC sumber (77, 78, 85); tidak ada penyimpangan (S-05, S-10). Unsuspend (TC-AUTH-SES-85) ditaruh paling akhir karena memulihkan state tenant.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 1 (menyiapkan halaman dengan form Search terisi), langkah 9 dan 15 (mengamati dialog yang menjadi precondition), langkah 18 (memajukan jam bersama dan menggerakkan mouse), dan langkah 21 (refresh atau navigasi).
- Expected butir c TC-AUTH-SES-77 ("tidak ada Session Log Entry baru dari Suspend", TC-AUTH-SES-195) adalah asersi absence dan tidak diasersikan di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi` (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-78 precondition b menyebut "form Search terisi" tanpa nilai; spec mengetik `Intan`. (2) TC-AUTH-SES-85 Expected b ("App Access kembali ke level sebelumnya") tidak menyebut cara memeriksa level App Access; spec memeriksa aksi tulis kembali tersedia dan tidak memilih halaman tertentu. (3) TC-AUTH-SES-77 tidak menyebut dialog konfirmasi saat memilih Suspend dan Unsuspend; spec mengikuti TC. (4) TC-AUTH-SES-78 mensyaratkan `Intan Lestari` (profil BASE) membuka `Global Settings > User`; izin halaman itu untuk profil BASE tidak dijelaskan di TC. (5) TC-AUTH-SES-77 b dan TC-AUTH-SES-85 b tidak menyebut permukaan pembacaan status sesi platform, sesi-produk, dan seat; spec memakai kemampuan BE yang disediakan tim FE/BE.