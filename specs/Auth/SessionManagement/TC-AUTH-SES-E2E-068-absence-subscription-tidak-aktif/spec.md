---
id: TC-AUTH-SES-E2E-068-absence-subscription-tidak-aktif
title: "Absence Pencatatan: Pembukaan Produk Diblok karena Subscription Tidak Aktif Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-113
  - TC-AUTH-SES-114
  - TC-AUTH-SES-115
  - TC-AUTH-SES-274
  - TC-AUTH-SES-275
  - TC-AUTH-SES-276
  - TC-AUTH-SES-277
  - TC-AUTH-SES-278
coverage:
  web: automated
---

# Absence Pencatatan: Pembukaan Produk Diblok karena Subscription Tidak Aktif Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Client uji status subscription (Tabel Data Uji Pre-setup #14): satu Client uji dengan subscription Fixed Asset Active di awal spec dipakai untuk enam status non-terminal (Archive, Waiting for Approval, Pending, Cancelled, Rejected, Converted); status terminal punya Client khusus satu per status: Client uji Purge (user `Reza Lestari`) dan Client uji Deleted (user `Sari Pratama`). Enam user lain milik Client uji. Status subscription dikondisikan per TC lewat langkah eksplisit "Atur status subscription ...": oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, bila status dicapai lewat aksi Admin Console atau lifecycle subscription, selain itu lewat seed BE yang disediakan tim BE (tanpa endpoint karangan). Jam server uji tidak digeser karena menggeser jam membuat sesi platform seluruh user uji dan sesi Browser Admin melewati batas idle.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client uji (Tabel Data Uji Pre-setup #31: Client Expired/uji, mencakup Client uji, Client uji Purge, dan Client uji Deleted) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): delapan user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run. Tidak ada sesi-produk Active milik user mana pun:
  - TC-AUTH-SES-113: `Mega Permata` (`megapermata+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-114: `Reza Lestari` (`rezalestari+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-115: `Sari Pratama` (`saripratama+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-274: `Agus Lestari` (`aguslestari+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-275: `Rina Pratama` (`rinapratama+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-276: `Hendra Ramadhan` (`hendraramadhan+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-277: `Maya Wulandari` (`mayawulandari+{runId}-068@qwertysystem.net`)
  - TC-AUTH-SES-278: `Fajar Hidayat` (`fajarhidayat+{runId}-068@qwertysystem.net`)
- Sesi platform web aktif per user, di Portal — Product Hub, dibuat di awal bagian TC masing-masing lewat login API (langkah penghubung), bukan di hook `before`, karena batas idle 15 menit berjalan selama spec berlangsung. Browser A pada tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuka pada langkah itu).
- Browser Admin: konteks browser yang memuat sesi akun aktor Total Control (Global Settings) scope Client uji (Tabel Data Uji Pre-setup #31) di atas (login pertama di hook `before`, sesudah seeding), dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`. Surface `Activity Log > Session` milik Fixed Asset yang disebut TC-AUTH-SES-274 s.d. 278 bertanda `[DEFERRED]` di TC; asersi absence untuk TC tersebut dibaca di `Global Settings > Activity Log > Session`.
- Entri "baru" dibedakan dari entri seeding (login sesi platform di awal bagian TC) lewat stempel waktu entri: hanya entri yang dibuat sesudah langkah klik card Fixed Asset pada TC itu yang dihitung.
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): pulihkan status subscription Fixed Asset Client uji ke Active (Client uji Purge dan Client uji Deleted berstatus terminal dan tidak dipulihkan; pembersihannya disediakan tim BE), akhiri semua sesi seed, tutup semua konteks browser (Browser A per user dan Browser Admin), hapus kedelapan user.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status subscription Fixed Asset Client uji pada Client uji (Active, Archive, Waiting for Approval, Pending, Cancelled, Rejected, Converted), dipulihkan di hook `after`; Client uji Purge dan Client uji Deleted dipakai satu kali dan tidak dipulihkan.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness g: asersi absence; kelas h: state tenant): pengaturan status subscription (termasuk status yang di-seed BE) per langkah oleh akun principal Admin Console; satu konteks browser per user uji ditambah Browser Admin bersamaan; pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A; akun aktor Total Control (Global Settings) di Browser Admin; akun aktor principal Admin Console untuk pengaturan status subscription.

## Test Steps

### TC-AUTH-SES-113 (bagian absence, Expected c): Subscription Archive tidak menulis entri log

1. Atur status subscription Fixed Asset Client uji menjadi Archive
2. Buat sesi web Active milik `Mega Permata` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
3. Di Browser A (sesi `Mega Permata`) klik card Fixed Asset → Popup Subscription Not Active tampil
4. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Mega Permata` yang dibuat sesudah langkah 17 dimulai
5. Verifikasi Tidak ada entri baru untuk `Mega Permata` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Archive
6. Buka `Global Settings > User > Detail > User Log` milik `Mega Permata` dan cari entri yang dibuat sesudah langkah 17 dimulai
7. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Archive

### TC-AUTH-SES-274 (bagian absence, Expected c): Subscription Waiting for Approval tidak menulis entri log

8. Atur status subscription Fixed Asset Client uji menjadi Waiting for Approval
9. Buat sesi web Active milik `Agus Lestari` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
10. Di Browser A (sesi `Agus Lestari`) klik card Fixed Asset → Popup Subscription Not Active tampil
11. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Agus Lestari` yang dibuat sesudah langkah 24 dimulai
12. Verifikasi Tidak ada entri baru untuk `Agus Lestari` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Waiting for Approval
13. Buka `Global Settings > User > Detail > User Log` milik `Agus Lestari` dan cari entri yang dibuat sesudah langkah 24 dimulai
14. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Waiting for Approval

### TC-AUTH-SES-275 (bagian absence, Expected c): Subscription Pending tidak menulis entri log

15. Atur status subscription Fixed Asset Client uji menjadi Pending
16. Buat sesi web Active milik `Rina Pratama` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
17. Di Browser A (sesi `Rina Pratama`) klik card Fixed Asset → Popup Subscription Not Active tampil
18. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Rina Pratama` yang dibuat sesudah langkah 31 dimulai
19. Verifikasi Tidak ada entri baru untuk `Rina Pratama` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Pending
20. Buka `Global Settings > User > Detail > User Log` milik `Rina Pratama` dan cari entri yang dibuat sesudah langkah 31 dimulai
21. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Pending

### TC-AUTH-SES-276 (bagian absence, Expected c): Subscription Cancelled tidak menulis entri log

22. Atur status subscription Fixed Asset Client uji menjadi Cancelled
23. Buat sesi web Active milik `Hendra Ramadhan` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
24. Di Browser A (sesi `Hendra Ramadhan`) klik card Fixed Asset → Popup Subscription Not Active tampil
25. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Hendra Ramadhan` yang dibuat sesudah langkah 38 dimulai
26. Verifikasi Tidak ada entri baru untuk `Hendra Ramadhan` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Cancelled
27. Buka `Global Settings > User > Detail > User Log` milik `Hendra Ramadhan` dan cari entri yang dibuat sesudah langkah 38 dimulai
28. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Cancelled

### TC-AUTH-SES-277 (bagian absence, Expected c): Subscription Rejected tidak menulis entri log

29. Atur status subscription Fixed Asset Client uji menjadi Rejected
30. Buat sesi web Active milik `Maya Wulandari` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
31. Di Browser A (sesi `Maya Wulandari`) klik card Fixed Asset → Popup Subscription Not Active tampil
32. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Maya Wulandari` yang dibuat sesudah langkah 45 dimulai
33. Verifikasi Tidak ada entri baru untuk `Maya Wulandari` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Rejected
34. Buka `Global Settings > User > Detail > User Log` milik `Maya Wulandari` dan cari entri yang dibuat sesudah langkah 45 dimulai
35. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Rejected

### TC-AUTH-SES-278 (bagian absence, Expected c): Subscription Converted tidak menulis entri log

36. Atur status subscription Fixed Asset Client uji menjadi Converted
37. Buat sesi web Active milik `Fajar Hidayat` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
38. Di Browser A (sesi `Fajar Hidayat`) klik card Fixed Asset → Popup Subscription Not Active tampil
39. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Fajar Hidayat` yang dibuat sesudah langkah 52 dimulai
40. Verifikasi Tidak ada entri baru untuk `Fajar Hidayat` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Converted
41. Buka `Global Settings > User > Detail > User Log` milik `Fajar Hidayat` dan cari entri yang dibuat sesudah langkah 52 dimulai
42. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Converted

### TC-AUTH-SES-114 (bagian absence, Expected c): Subscription Purge tidak menulis entri log

43. Atur status subscription Fixed Asset Client uji Purge menjadi Purge
44. Buat sesi web Active milik `Reza Lestari` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
45. Di Browser A (sesi `Reza Lestari`) klik card Fixed Asset → Popup Subscription Not Active tampil
46. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Reza Lestari` yang dibuat sesudah langkah 59 dimulai
47. Verifikasi Tidak ada entri baru untuk `Reza Lestari` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Purge
48. Buka `Global Settings > User > Detail > User Log` milik `Reza Lestari` dan cari entri yang dibuat sesudah langkah 59 dimulai
49. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Purge

### TC-AUTH-SES-115 (bagian absence, Expected c): Subscription Deleted tidak menulis entri log

50. Atur status subscription Fixed Asset Client uji Deleted menjadi Deleted
51. Buat sesi web Active milik `Sari Pratama` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
52. Di Browser A (sesi `Sari Pratama`) klik card Fixed Asset → Popup Subscription Not Active tampil
53. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Sari Pratama` yang dibuat sesudah langkah 66 dimulai
54. Verifikasi Tidak ada entri baru untuk `Sari Pratama` di `Global Settings > Activity Log > Session` untuk kondisi pembukaan produk diblok karena subscription Deleted
55. Buka `Global Settings > User > Detail > User Log` milik `Sari Pratama` dan cari entri yang dibuat sesudah langkah 66 dimulai
56. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription Deleted

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness g (asersi absence) dengan state tenant kelas h. Spec ini melewati batas sekitar 35 langkah karena delapan TC berpola identik (satu status subscription per TC); bagian sesudah tiap TC tidak bergantung pada TC sebelumnya (user, Browser A, dan jendela waktu entri berbeda per TC).
- Pembagian TC lintas spec (prinsip 10): sisi fungsional TC-AUTH-SES-113 (Popup, 403, sesi-produk tidak dibuat, halaman tidak dimuat) ada di spec `TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk`; sisi fungsional TC-AUTH-SES-114, 115, dan 274 s.d. 278 ada di spec `TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk`. Spec ini hanya memuat Expected c (asersi absence, S-05); asersi fungsional tidak diulang. Tiap TC memakai user bersuffix `-068` sendiri, tidak menumpang user spec 036 dan 037. Spec `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi` memuat TC-AUTH-SES-202 (pembukaan produk diblok karena subscription tidak aktif, Client dengan subscription Archive); bagian TC-AUTH-SES-113 s.d. 115 dan 274 s.d. 278 di spec ini tidak menduplikasi bagian TC-AUTH-SES-202 karena TC-nya berbeda (status, user, dan id TC berbeda).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 113, 274, 275, 276, 277, 278, 114, 115 (urutan TC sumber 113, 114, 115, 274 s.d. 278). Status Purge dan Deleted adalah akhir lifecycle subscription sehingga ditaruh paling akhir; status lain diubah per TC tanpa bolak-balik. TC-AUTH-SES-111 dan TC-AUTH-SES-112 (Expired, Grace) tidak ada di spec ini: pembukaan produk pada status itu tidak ditolak dan tercatat `Session started` (spec `TC-AUTH-SES-E2E-077-expired-grace-buka-produk-tanpa-popup`).
- Langkah dependensi disalin (S-04): tiap bagian menyalin langkah pemicu minimal sampai kejadian yang seharusnya tidak dicatat terjadi, yaitu pengondisian status subscription dan klik card Fixed Asset sampai Popup Subscription Not Active tampil (langkah 1–3, 8–10, 15–17, 22–24, 29–31, 36–38, 43–45, 50–52). Asersi hasilnya (isi Popup, 403, sesi-produk tidak dibuat, halaman tidak dimuat) diuji di spec 036 dan 037.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "Atur status subscription ..." mengondisikan state tenant; perpindahan ke Browser Admin dan pembukaan surface log beserta pencarian entri. Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah klik card Fixed Asset pada TC itu yang dihitung (langkah 3, 10, 17, 24, 31, 38, 45, 52).
- Surface Fixed Asset `[DEFERRED]`: TC-AUTH-SES-274 s.d. 278 menyebut `Activity Log > Session` milik Fixed Asset dengan tanda `[DEFERRED]` (forward-dependency, NC-15). Sesuai keputusan, asersi absence untuk kelima TC dibaca di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`. Bila surface Fixed Asset tersedia, tambahkan langkah baca di sana pada bagian TC-AUTH-SES-274 s.d. 278.
- Temuan untuk QA:
  - TC-AUTH-SES-113 s.d. 115 dan 274 s.d. 278 tidak menyebut baris log awal (anchor) untuk user uji; spec membedakan entri baru lewat stempel waktu setelah klik card Fixed Asset (login sesi platform di awal bagian TC menulis entri sendiri).
  - TC-AUTH-SES-113 s.d. 115 dan 274 s.d. 278 menulis user dan Client "dengan subscription ... berstatus X (Tabel Data Uji Pre-setup #14)" tanpa menyebut cara memicu status itu; spec memakai satu Client uji yang statusnya diatur akun principal Admin Console per langkah (mengikuti spec 036 dan 037). Kemampuan akun Total Control (Tabel Data Uji Pre-setup #31, scope Client Expired/uji) membaca log user pada kondisi subscription Fixed Asset tidak aktif tidak dinyatakan di TC; spec mengasumsikan akses Global Settings tidak ikut terblok oleh status subscription Fixed Asset dan scope #31 mencakup Client uji, Client uji Purge, dan Client uji Deleted (Client terminal khusus satu per status; perlu konfirmasi QA/BE).
  - TC-AUTH-SES-274 s.d. 278 menandai `[DEFERRED]` di ujung kalimat Expected c sehingga tidak jelas apakah User Log (surface Global Settings) ikut ditunda; spec mengasersi User Log dan Global Settings Activity Log > Session, dan hanya surface Fixed Asset yang ditunda. Kolom Automation TC-AUTH-SES-274 s.d. 278 bernilai `Manual Only` dan kolom Dependensi berisi `[DEFERRED]`; spec tetap memuatnya (hambatan teknis bukan alasan mengeluarkan TC).
