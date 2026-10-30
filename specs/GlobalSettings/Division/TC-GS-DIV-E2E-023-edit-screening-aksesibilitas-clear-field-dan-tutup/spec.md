---
id: TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup
title: "Edit Division: Screening Popup, Aksesibilitas, Clear Field, dan Tutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-81
  - TC-GS-DIV-291
  - TC-GS-DIV-105
  - TC-GS-DIV-106
  - TC-GS-DIV-107
  - TC-GS-DIV-108
coverage:
  web: automated
---

# Edit Division: Screening Popup, Aksesibilitas, Clear Field, dan Tutup

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku popup Edit di browser.
- Kebutuhan mock (endpoint dari `low-level-design.md`):
  - Sesi dan payload izin akun Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` dengan Access Level Total Control. Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD` (nilai tidak ditulis di spec).
  - Respons `POST /v2/iam/divisions/list`: memuat Division `Accounting` (Code `ACC`).
  - Respons `POST /v2/iam/divisions/check-availability` (cek keunikan Name dan Code saat mengetik, debounce ±500 ms): tersedia untuk semua nilai yang diketik, sehingga tidak ada error duplikat.
  - Stream SSE tab Division (PRD `division.md` bagian Sync + Realtime; LLD `API/low-level-design.md` L159, L256, L347 hanya menyebut event `division.created`, `division.updated`, `division.deleted` tanpa path endpoint, sehingga path stream disediakan tim FE): koneksi stream di-mock tetap terbuka dan tidak mengirim event apa pun selama spec, sehingga tidak ada refetch atau perubahan data tabel.
  - Respons sesi/profil, menu, dan flag Guided Tooltip `guided_tooltip_seen_gs-division` (sudah dilihat): disediakan tim FE (API di luar sumber modul).
  - Request simpan Edit (`PATCH /v2/iam/divisions/{division_id}`) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (Save pada langkah 13 diblokir validasi Name kosong dan tidak ada TC lain yang men-submit).
- Data: memakai Division mock `Accounting` (`ACC`); tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup.
- Kemampuan teknis: penekanan Tab dan Esc; membaca elemen yang sedang fokus; membaca atribut `aria-required` dan `aria-describedby` pada field; mendeteksi muncul tidaknya dialog.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` dengan respons mock di atas.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: spec `Mode: mock`, flag diatur lewat respons mock yang tertulis di atas (hook suite tidak berlaku, `suite.md`).
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control), sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-DIV-81 dan TC-GS-DIV-291 (bagian fokus awal): Screening Popup Edit Division

1. Buka row action baris `Accounting` lalu klik `Edit`
2. Verifikasi kursor otomatis fokus pada input Division Name
3. Verifikasi Header: Title `Edit Division`
4. Verifikasi Header: icon close `[✕]`
5. Verifikasi Body: field `Division Name *` terisi `Accounting`
6. Verifikasi Body: field `Code` terisi `ACC`
7. Verifikasi Body: helper text Code `Letters, numbers, hyphens, underscores, and dots only`
8. Verifikasi Body: checkbox `Stay on this form after submitting` tidak tampil
9. Verifikasi Footer: tombol `[Clear Field]` dan `[Save]` tampil
10. Verifikasi Footer: tombol `[Clear Field]` dan `[Save]` rata kanan
11. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-DIV-291 (bagian aria, focus trap, dan Esc): Accessibility Popup Edit Division

12. Kosongkan Division Name
13. Klik `[Save]`
14. Verifikasi field Division Name memiliki `aria-required="true"`
15. Verifikasi error field Division Name terhubung lewat `aria-describedby`
16. Isi kembali Division Name `Accounting`
17. Tekan Tab berulang melewati seluruh elemen di modal Edit
18. Verifikasi fokus keyboard tidak keluar dari modal (focus trap)
19. Tekan Esc
20. Verifikasi modal Edit tertutup
21. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-DIV-106: Menutup form Edit tanpa perubahan tidak memunculkan dialog Unsaved Changes

22. Buka row action baris `Accounting` lalu klik `Edit`
23. Klik icon close `[✕]`
24. Verifikasi modal langsung tertutup
25. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-DIV-105: Clear Field pada Edit mengosongkan field tanpa me-revert nilai tersimpan

26. Buka row action baris `Accounting` lalu klik `Edit`
27. Klik `[Clear Field]`
28. Verifikasi Division Name kosong (bukan kembali ke nilai tersimpan)
29. Verifikasi Code kosong (bukan kembali ke nilai tersimpan)
30. Verifikasi tidak ada dialog Unsaved Changes
31. Verifikasi modal tetap terbuka

### TC-GS-DIV-107: Close Edit saat dirty lalu Cancel mempertahankan form

32. Ubah Division Name menjadi `Draft Edit`
33. Klik icon close `[✕]`
34. Verifikasi dialog `Unsaved Changes` tampil
35. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
36. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
37. Klik `[Cancel]`
38. Verifikasi modal Edit tetap terbuka
39. Verifikasi Division Name tetap `Draft Edit`

### TC-GS-DIV-108: Close Edit saat dirty lalu Leave membuang perubahan

40. Klik icon close `[✕]`
41. Verifikasi dialog `Unsaved Changes` tampil
42. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
43. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
44. Klik `[Leave]`
45. Verifikasi modal Edit tertutup
46. Verifikasi Division Name `Accounting` pada baris di tabel tidak berubah

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-81, 291, 105, 106, 107, 108). Mode: mock. Kelas harness: screening UI.
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC di spec berbeda dari urutan sumber (81, 291, 105, 106, 107, 108) dan memakai tiga pembukaan form (prinsip 6): pembukaan pertama untuk TC-GS-DIV-81 dan TC-GS-DIV-291 (fokus awal dan screening diperiksa saat form baru terbuka sebelum interaksi, lalu aria, focus trap, dan Esc, dan form ditutup bersih lewat Esc karena nilai dikembalikan ke `Accounting`); pembukaan kedua untuk TC-GS-DIV-106 (tutup bersih lewat `[✕]`); pembukaan ketiga untuk TC-GS-DIV-105, TC-GS-DIV-107, dan TC-GS-DIV-108 (form yang dikosongkan lewat `[Clear Field]` tidak dihitung bersih, sehingga dipakai untuk kasus tutup dirty).
- TC-GS-DIV-107 dan TC-GS-DIV-108 melanjutkan form dari TC-GS-DIV-105 (Name dan Code kosong, lalu Name diisi `Draft Edit` dengan Code tetap kosong). Keadaan dirty tetap terpenuhi, dan TC tidak menyebut nilai Code.
- Langkah penghubung (aksi tanpa `Verifikasi` yang bukan langkah TC): tidak ada. Langkah 12, 13, 16, 17, dan 19 adalah langkah 3 sampai 5 TC-GS-DIV-291 (kosongkan Name, klik `[Save]`, isi kembali `Accounting`, Tab berulang, Esc).
- Langkah 38 dan 39 memeriksa kondisi sesudah `[Cancel]`; langkah 40 menutup form yang masih dirty lewat `[✕]` untuk TC-GS-DIV-108 tanpa membuka ulang.
- Temuan untuk QA:
  - TC-GS-DIV-291 butir b tidak menyebut teks error field Name yang tampil setelah `[Save]` dengan Name kosong; spec hanya mengasersi atribut aria.
  - TC-GS-DIV-291 langkah 4 ("Tab berulang melewati seluruh elemen") tidak menyebut jumlah penekanan Tab; spec menafsirkan satu putaran penuh dan lebih.
  - Post Condition TC-GS-DIV-105 ("Name dan Code Accounting di database tidak berubah") tidak punya langkah observasi di TC dan pada mode mock tidak ada state backend; tidak diasersi.
- Spec melewati sekitar 35 langkah (46 langkah) karena memuat enam TC screening dan penutupan form pada satu popup yang sama, satu kelas harness (screening UI, mode mock), dan tiap blok TC berdiri sendiri dengan form yang dibuka ulang atau dilanjutkan sesuai keadaan dirty-nya.
