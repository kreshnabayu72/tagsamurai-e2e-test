---
id: TC-FA-CF-E2E-131-absence-log-save-no-op
title: "Absence Log: Save No-Op Tidak Menulis Entri di Tiga Surface"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-220
  - TC-FA-CF-221
  - TC-FA-CF-222
  - TC-FA-CF-504
coverage:
  web: automated
---

# Absence Log: Save No-Op Tidak Menulis Entri di Tiga Surface

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 40): Total Control Company Alpha, pengguna Sarah Johnson (Pre-setup #1) dengan `Spectra.env.FA_TC_PASSWORD`; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12, Max custom fields per asset name 20) dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diedit tanpa perubahan bermakna: `Storage Capacity` (Numeric 0 Decimal Places, Scope Generator dan Pump). TC-FA-CF-504 memakai Company Alpha (Pre-setup #11 dan #12) dengan baris `Storage Capacity` yang sama.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-220: Save no-op tidak menulis entri log di tiga surface

1. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Klik `[Save]` tanpa mengubah apa pun
4. Tunggu aksi selesai (modal Edit tertutup)
5. Buka Modal Changelog tab General dan hitung ulang jumlah entri
6. Verifikasi jumlah entri Changelog tab General sama dengan baseline
7. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
8. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
9. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
10. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-221: Edit Field Name yang hanya mengubah kapitalisasi adalah no-op

11. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
12. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
13. Ubah Field Name menjadi `STORAGE CAPACITY`
14. Klik `[Save]`
15. Verifikasi modal Edit tertutup
16. Verifikasi toast netral `No changes to save.` tampil
17. Verifikasi toast `Success, custom field has been updated.` tidak tampil
18. Verifikasi Field Name tersimpan tetap `Storage Capacity` pada tabel
19. Buka Modal Changelog tab General dan hitung ulang jumlah entri
20. Verifikasi jumlah entri Changelog tab General sama dengan baseline
21. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
22. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
23. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
24. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-222: Pemulihan Data Type tersimpan sebelum Save membuat Save adalah no-op

25. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
26. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
27. Ganti Data Type menjadi `Text`
28. Pilih kembali Data Type `Numeric`
29. Verifikasi Decimal Places tersimpan dipulihkan
30. Verifikasi Dropdown Options tersimpan dipulihkan
31. Klik `[Save]`
32. Verifikasi toast netral `No changes to save.` tampil
33. Verifikasi dialog `Change Data Type` tidak tampil
34. Buka Modal Changelog tab General dan hitung ulang jumlah entri
35. Verifikasi jumlah entri Changelog tab General sama dengan baseline
36. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
37. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
38. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
39. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-504: Edit No-Op menulis nol entri di tiga surface

40. Ganti akun: logout, lalu login sebagai Total Control Company Alpha (Pre-setup #1)
41. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
42. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`, lalu klik `[Save]` tanpa perubahan
43. Tunggu aksi selesai (modal Edit tertutup)
44. Buka Modal Changelog tab General dan hitung ulang jumlah entri
45. Verifikasi jumlah entri Changelog tab General sama dengan baseline
46. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
47. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
48. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
49. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 49 langkah bernomor; langkah blok baca-log berpola (buka surface, temukan baris, `Verifikasi` kolom log; 24 langkah, nomor 5 sampai 10, 19 sampai 24, 34 sampai 39, 44 sampai 49) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 25 langkah. Spec dipertahankan karena semua blok satu kelas harness (asersi absence log) dengan pemicu aksi nyata (Save tanpa perubahan); tiap TC punya baseline sendiri (P-5 butir a).
- P-5 (a): spec absence kelas g; pemicu (Save tanpa perubahan, Save Field Name yang hanya berbeda kapitalisasi, pemulihan Data Type sebelum Save) adalah aksi UI biasa dan bukan objek uji; tiap TC memakai baseline jumlah entri sendiri (S-12).
- Urutan TC di spec: 220, 221, 222, 504. TC-FA-CF-504 berjalan terakhir di Company Alpha dan memerlukan ganti akun eksplisit (langkah 40). TC-FA-CF-220, 221, dan 222 memakai Company Nilai.
- Anchor positif (8b butir 2): jumlah entri awal yang dicatat pada langkah baseline tiap TC dan, untuk TC-FA-CF-221 dan TC-FA-CF-222, toast netral `No changes to save.` yang diasersi sebelum pembacaan log; asersi "tidak ada entri baru" ditulis sebagai kesamaan jumlah entri dengan baseline di tiap surface.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 40, baseline, "Tunggu aksi selesai", serta langkah buka surface dan hitung ulang jumlah entri.
- Temuan untuk QA:
  - TC-FA-CF-222 Expected b ("Decimal Places dan Dropdown Options tersimpan dipulihkan") tidak menyebut nilai yang diharapkan; `Storage Capacity` bertipe Numeric 0 Decimal Places dan tidak memiliki opsi Dropdown tersimpan, sehingga asersi Dropdown Options tidak punya nilai konkret.
  - TC-FA-CF-504 memakai Company Alpha, sedangkan TC-FA-CF-220 sampai 222 memakai Company Nilai dengan field `Storage Capacity` yang sama; spec mengikuti precondition TC masing-masing sehingga ganti akun diperlukan.
  - TC-FA-CF-220 dan TC-FA-CF-504 tidak menyebut toast netral; spec tidak mengasersinya untuk kedua TC itu.
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
