---
id: TC-AC-ACC-E2E-074-edit-konkurensi-pelaku-kedua-api-last-write-dihapus-suspend-aktivasi-af
title: "Edit Client dengan Perubahan Pelaku Kedua: Last-Write-Wins, Client Dihapus, Client Di-Suspend, dan Default User Diaktivasi (Active-Full)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-163
  - TC-AC-ACC-636
  - TC-AC-ACC-637
  - TC-AC-ACC-544
coverage:
  web: automated
---

# Edit Client dengan Perubahan Pelaku Kedua: Last-Write-Wins, Client Dihapus, Client Di-Suspend, dan Default User Diaktivasi (Active-Full)

## Prerequisites

- Mode: FE+BE. Pelaku kedua memakai sesi API (bukan sesi UI kedua).
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Dataset seed (nama bersuffix): `PT Direct Jakarta {runId}-074` (replika C-ROL-13: Direct, Group Area Jakarta, PIC Name awal `Budi Hartono`), `PT Uji Konkurensi 02 {runId}-074` (replika C-LIF-20: Active), `PT Uji Konkurensi 05 {runId}-074` (replika C-LIF-23: Active, Fax awal tercatat), `PT Aktivasi Uji {runId}-074` (replika C-EDT-3: Active, FAMS Active, Default User Not Yet Activated `Dewi Anggraini`, `dewi.anggraini+{runId}-074@qwertysystem.net`, Activation Email dapat diambil dari mail-catcher). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Kemampuan teknis: sesi API aktor Active-Full untuk mengubah PIC Name, menghapus Client, dan men-suspend Client (tidak dihitung sebagai sesi web); mail-catcher untuk mengambil tautan Activation Email; membuka tautan itu di konteks browser kedua untuk mengaktifkan akun Default User (hanya pemicu); membaca status respons request Edit.
- Cleanup: hook `after` menghapus Client seed lewat API dan menutup konteks browser kedua; `PT Uji Konkurensi 05 {runId}-074` dipulihkan ke Active bila masih Suspended.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-163: Dua admin mengedit field yang sama, last-write-wins

1. Ketik Search `PT Direct Jakarta {runId}-074`, tekan Enter
2. Buka `⋯` baris `PT Direct Jakarta {runId}-074` lalu klik `Edit`
3. Pelaku kedua (sesi API) mengubah PIC Name "PT Direct Jakarta {runId}-074" menjadi "Alfa Pratama" hingga tersimpan
4. Tunggu aksi selesai
5. Ubah PIC Name menjadi "Beta Santoso"
6. Klik `[Save]`
7. Verifikasi toast sukses "Success, client has been updated."
8. Verifikasi tidak ada dialog konflik
9. Klik Company Name `PT Direct Jakarta {runId}-074` untuk membuka Detail
10. Verifikasi Detail menampilkan PIC Name "Beta Santoso"
11. Klik breadcrumb "Client" untuk kembali ke List

### TC-636: Client dihapus admin lain

12. Ketik Search `PT Uji Konkurensi 02 {runId}-074`, tekan Enter
13. Buka `⋯` baris `PT Uji Konkurensi 02 {runId}-074` lalu klik `Edit`
14. Ubah Fax menjadi `0215550199`
15. Pelaku kedua (sesi API) menghapus Client "PT Uji Konkurensi 02 {runId}-074" hingga terhapus
16. Tunggu aksi selesai
17. Klik `[Save]`
18. Verifikasi toast netral "This client is no longer available."
19. Verifikasi toast error "Error, failed to update client." tidak tampil
20. Ketik Search `PT Uji Konkurensi 02 {runId}-074`, tekan Enter
21. Verifikasi List sub-tab Active disegarkan dan baris "PT Uji Konkurensi 02 {runId}-074" tidak tampil

### TC-637: Client di-Suspend admin lain

22. Ketik Search `PT Uji Konkurensi 05 {runId}-074`, tekan Enter
23. Klik Company Name `PT Uji Konkurensi 05 {runId}-074` untuk membuka Detail dan catat nilai Fax (F0)
24. Klik breadcrumb "Client" untuk kembali ke List
25. Ketik Search `PT Uji Konkurensi 05 {runId}-074`, tekan Enter
26. Buka `⋯` baris `PT Uji Konkurensi 05 {runId}-074` lalu klik `Edit`
27. Ubah Fax menjadi `0215550188`
28. Pelaku kedua (sesi API) men-suspend Client "PT Uji Konkurensi 05 {runId}-074" hingga berstatus Suspended
29. Tunggu aksi selesai
30. Klik `[Save]`
31. Verifikasi respons request Edit 403 Forbidden
32. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
33. Verifikasi toast "Error, failed to update client." tidak tampil
34. Verifikasi popup Edit tertutup
35. Verifikasi List sub-tab Active di-refresh dan baris "PT Uji Konkurensi 05 {runId}-074" tidak lagi tampil di sub-tab Active
36. Klik sub-tab Suspended
37. Ketik Search `PT Uji Konkurensi 05 {runId}-074`, tekan Enter
38. Verifikasi "PT Uji Konkurensi 05 {runId}-074" tampil di sub-tab Suspended
39. Klik Company Name `PT Uji Konkurensi 05 {runId}-074` untuk membuka Detail
40. Verifikasi Detail menampilkan Fax F0 (bukan `0215550188`)
41. Klik breadcrumb "Client" untuk kembali ke List

### TC-544: Default User diaktivasi sebelum Save

42. Klik sub-tab Active
43. Ketik Search `PT Aktivasi Uji {runId}-074`, tekan Enter
44. Buka `⋯` baris `PT Aktivasi Uji {runId}-074` lalu klik `Edit`
45. Ubah First Name Default User menjadi "Dewi Ayu"
46. Pelaku kedua membuka tautan Activation Email Default User "PT Aktivasi Uji {runId}-074" dari mail-catcher di konteks browser kedua dan mengaktifkan akun hingga status Activated
47. Tunggu aksi selesai
48. Klik `[Save]`
49. Verifikasi toast error "Error, failed to update client."
50. Verifikasi popup tetap terbuka
51. Klik `[✕]` di header popup
52. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
53. Klik `[Leave]`
54. Klik Company Name `PT Aktivasi Uji {runId}-074` untuk membuka Detail
55. Verifikasi section Default User menampilkan Name "Dewi Anggraini" (tidak berubah)
56. Verifikasi section Default User menampilkan status "Activated"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 60 langkah): satu role, satu topik (Edit saat state Client berubah oleh pelaku kedua), empat Client seed milik sendiri; tiap blok berdiri sendiri.
- Pelaku kedua TC-163, TC-636, dan TC-637 memakai sesi API hingga perubahan tersimpan (R-20); bukan konteks UI kedua, sehingga tidak butuh butir `P-2`. `P-2` (TC-544): konteks browser kedua hanya memicu aktivasi Default User lewat tautan Activation Email dan tidak diasersi; objek asersi tetap sesi Active-Full.
- Langkah penghubung (S-03): "Tunggu aksi selesai" sesudah aksi pelaku kedua (butir 8b-8), Search nama unik, sub-tab, breadcrumb "Client", dan penutup form dirty (S-08).
- Temuan untuk QA:
  - TC-163, TC-636, TC-637, dan TC-544 bertanda Manual Only (dua sesi paralel); perubahan sesi kedua yang di TC dilakukan lewat UI (mis. Delete dengan ketik nama persis di TC-636) dilakukan lewat sesi API di spec ini sesuai konvensi (pelaku kedua hanya memicu perubahan state).
  - TC-637 mensyaratkan respons 403 diamati di browser; kemampuan membaca status respons ditulis di Prerequisites.
