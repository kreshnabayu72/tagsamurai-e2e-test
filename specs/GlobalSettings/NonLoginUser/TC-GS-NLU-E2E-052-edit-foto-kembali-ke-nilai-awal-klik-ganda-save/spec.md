---
id: TC-GS-NLU-E2E-052-edit-foto-kembali-ke-nilai-awal-klik-ganda-save
title: "Edit: foto, kembali ke nilai awal, klik ganda Save"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-167
  - TC-GS-NLU-168
  - TC-GS-NLU-170
  - TC-GS-NLU-171
  - TC-GS-NLU-180
coverage:
  web: automated
---

# Edit: foto, kembali ke nilai awal, klik ganda Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position, Division (Operations), dan pool Login User Represented By (Ahmad Fauzi).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Non-Login User Edit Target 26 (TC-GS-NLU-167 dan TC-GS-NLU-168, tanpa foto), Edit Target 29 (TC-GS-NLU-170), Edit Target 30 (TC-GS-NLU-171), dan Edit Target 47 (TC-GS-NLU-180, memiliki foto). Setiap target: First Name `Edit Target NN`, Last Name `{runId}-052`, Email `edittargetNN+{runId}-052@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active. TC-GS-NLU-167 dan TC-GS-NLU-168 memakai satu target dan satu pembukaan popup karena tidak ada Save yang berhasil (Edit Target 26 dan 27 pada TC).
- Berkas uji di perangkat uji (fixture belum ada; disediakan tim FE): PNG 12 MB, JPG 5 MB, PNG 200 KB.
- Kemampuan teknis: jumlah permintaan simpan yang terkirim pada klik ganda dihitung lewat penangkapan permintaan jaringan (`Spectra.intercept()` atau setara); Recycle Bin File Manager dibaca lewat UI. Baseline entri Edit pada Tab Changelog Edit Target 30 adalah nol karena record baru di-seed tanpa entri Edit (baseline nol lewat data milik spec, S-12).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target 26 {runId}-052`, tekan Enter
2. Klik `⋯` pada baris Edit Target 26 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-167: Unggah foto lebih dari 10 MB ditolak dengan toast pada Popup Edit

3. Unggah berkas PNG 12 MB pada avatar
4. Verifikasi toast error `Error, failed to upload photo.`
5. Verifikasi foto tidak dipilih dan avatar tetap placeholder

### TC-GS-NLU-168: Unggah foto 1 MB sampai 10 MB dikompres otomatis tanpa error pada Popup Edit

6. Tutup toast error sebelumnya
7. Unggah berkas JPG 5 MB pada avatar
8. Verifikasi foto tampil sebagai avatar bulat
9. Verifikasi tidak ada pesan error
10. Klik `✕` pada Popup Edit Non-Login User
11. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
12. Klik `[Leave]`

### TC-GS-NLU-170: Mengubah field lalu mengembalikannya ke nilai awal dianggap belum diubah pada Popup Edit

13. Ganti isi kotak search dengan `Edit Target 29 {runId}-052`, tekan Enter
14. Klik `⋯` pada baris Edit Target 29 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
15. Ubah First Name
16. Kembalikan First Name persis ke nilai awal
17. Klik `✕`
18. Verifikasi Popup Edit langsung tertutup
19. Verifikasi tidak ada dialog Unsaved Changes

### TC-GS-NLU-171: Klik ganda cepat pada tombol Save hanya diproses sekali pada Popup Edit

20. Ganti isi kotak search dengan `Edit Target 30 {runId}-052`, tekan Enter
21. Klik `⋯` pada baris Edit Target 30 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
22. Ubah First Name menjadi `Hari2`
23. Klik ganda cepat `[Save]`
24. Verifikasi tombol langsung masuk Saving state setelah klik pertama
25. Verifikasi hanya satu permintaan simpan yang diproses
26. Verifikasi satu toast sukses tampil
27. Buka Detail Edit Target 30 > tab `Changelog`
28. Verifikasi Tab Changelog memuat tepat satu entri Edit untuk perubahan First Name
29. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-180: Edit mengganti foto lalu menghapus foto menampilkan avatar baru lalu placeholder

30. Ganti isi kotak search dengan `Edit Target 47 {runId}-052`, tekan Enter
31. Klik `⋯` pada baris Edit Target 47 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
32. Hover avatar, ganti dengan foto PNG 200 KB
33. Klik `[Save]`
34. Verifikasi toast sukses `Success, non-login user has been updated.`
35. Verifikasi baris Edit Target 47 di tabel menampilkan foto baru
36. Buka Detail Edit Target 47
37. Verifikasi Detail menampilkan foto baru
38. Kembali ke daftar Non-Login User lewat breadcrumb
39. Klik `⋯` pada baris Edit Target 47 > `Edit` sehingga Popup Edit Non-Login User terbuka
40. Hover avatar
41. Verifikasi overlay avatar menampilkan `[Edit]` dan `[Delete]`
42. Klik `[Delete]` pada overlay
43. Verifikasi avatar pada form menjadi placeholder generik
44. Verifikasi tidak ada dialog konfirmasi
45. Klik `[Save]`
46. Verifikasi avatar baris Edit Target 47 di tabel kembali ke placeholder generik
47. Buka File Manager > Recycle Bin dan cari berkas foto lama
48. Verifikasi Recycle Bin memuat dua berkas: foto asli dan foto pengganti
49. Buka Detail Edit Target 47 > tab `Changelog`
50. Verifikasi Tab Changelog mencatat `Edit` Field `Photo`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Spec ini melewati sekitar 35 langkah (nominal 49). Alasan: kelima TC berdiri sendiri dengan target milik spec masing-masing (Edit Target 26, 29, 30, 47), dan hasil satu blok tidak dipakai blok lain sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; TC-GS-NLU-180 sendiri memuat empat tahap (ganti foto, hapus foto, Recycle Bin, Changelog).
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 13, 20, dan 30 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List); langkah 6 (menutup toast error TC-GS-NLU-167 supaya asersi tidak ada pesan error TC-GS-NLU-168 tidak terpengaruh, R-12); langkah 10 sampai 12 (menutup popup yang dirty secara deterministik, S-08); langkah 29 dan 38 (kembali ke daftar setelah Detail).
- Temuan untuk QA:
  - TC-GS-NLU-167 Expected butir b ("foto sebelumnya (bila ada) tidak berubah") bersyarat; target Edit Target 26 sengaja tanpa foto sehingga hanya "foto tidak dipilih" yang diasersi.
  - TC-GS-NLU-171 Expected butir b ("Hanya satu perubahan tercatat") tidak menyebut tempat pencatatan; spec memakai Tab Changelog Detail dengan baseline nol entri Edit.
  - TC-GS-NLU-180 Expected butir d memuat dua berkas di Recycle Bin dengan "soft-delete saat langkah 2 dan 4", tanpa menyebut nama berkas; spec mengasersi jumlah dua berkas hasil pencarian berkas foto lama.
  - TC-GS-NLU-180 Expected butir b ("baru tersimpan saat `[Save]`") tidak menyebut cara membuktikan foto belum terhapus sebelum Save; spec mengasersi hanya avatar pada form setelah `[Delete]` dan avatar baris setelah `[Save]`.
