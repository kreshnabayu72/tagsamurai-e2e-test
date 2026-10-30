---
id: TC-GS-DIV-E2E-019-create-unsaved-changes-dialog
title: "Create Division: Dialog Unsaved Changes (X, Esc, Cancel, Leave, Backdrop)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-68
  - TC-GS-DIV-69
  - TC-GS-DIV-70
  - TC-GS-DIV-71
coverage:
  web: automated
---

# Create Division: Dialog Unsaved Changes (X, Esc, Cancel, Leave, Backdrop)

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji perilaku menutup modal Create Division yang dirty.
- Kebutuhan mock:
  - Sesi dan payload izin akun Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan Access Level Total Control. Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD` (nilai tidak ditulis di spec).
  - Respons `POST /v2/iam/divisions/list`: 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury), tanpa `Draft Division`, supaya tabel Division dan tombol `[+ Division]` tampil.
  - Respons `POST /v2/iam/divisions/check-availability` (cek keunikan Division Name saat mengetik, debounce sekitar 500 ms): nama tersedia untuk `Draft Division`, sehingga tidak ada error duplikat yang muncul.
  - Stream SSE tab Division (PRD `division.md` bagian Sync + Realtime; LLD `API/low-level-design.md` L159, L256, L347 hanya menyebut event `division.created`, `division.updated`, `division.deleted` tanpa path endpoint, sehingga path stream disediakan tim FE): koneksi stream di-mock tetap terbuka dan tidak mengirim event apa pun selama spec, sehingga tidak ada refetch atau perubahan data tabel.
  - Respons sesi/profil, menu, dan flag Guided Tooltip `guided_tooltip_seen_gs-division` (sudah dilihat): disediakan tim FE (API di luar sumber modul).
  - Endpoint `POST /v2/iam/divisions` (Create Division) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit).
- Data: nilai `Draft Division` hanya diketik dan tidak pernah tersimpan, sehingga tidak ada seeding dan tidak ada cleanup.
- Kemampuan teknis: penekanan Esc; klik pada area backdrop di luar modal; pembacaan severity dan teks dialog; pembacaan nilai field.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` dengan respons mock di atas.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: spec `Mode: mock`, flag diatur lewat respons mock yang tertulis di atas (hook suite tidak berlaku, `suite.md`).
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control, Sari Dewi), sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-DIV-70: Close via tombol Escape saat form dirty menampilkan dialog

1. Klik `[+ Division]`
2. Ketik `Draft Division` pada field Division Name
3. Tekan Esc
4. Verifikasi dialog `Unsaved Changes` (severity warning) tampil
5. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
6. Verifikasi tombol `[Cancel]` tampil pada dialog
7. Verifikasi tombol `[Leave]` tampil pada dialog
8. Klik `[Cancel]`
9. Verifikasi modal Create tetap terbuka
10. Verifikasi input Division Name dipertahankan: `Draft Division`

### TC-GS-DIV-68: Close via icon X saat form dirty lalu Cancel mempertahankan form

11. Klik icon close `[✕]`
12. Verifikasi dialog `Unsaved Changes` (severity warning) tampil
13. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
14. Verifikasi tombol `[Cancel]` tampil pada dialog
15. Verifikasi tombol `[Leave]` tampil pada dialog
16. Klik `[Cancel]`
17. Verifikasi dialog tertutup
18. Verifikasi modal Create tetap terbuka
19. Verifikasi Division Name tetap `Draft Division`

### TC-GS-DIV-71: Klik backdrop saat form dirty tidak menutup form

20. Klik area backdrop di luar modal
21. Verifikasi modal Create tetap terbuka
22. Verifikasi Division Name tetap `Draft Division`
23. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-GS-DIV-69: Close via icon X saat form dirty lalu Leave membuang input

24. Klik icon close `[✕]`
25. Verifikasi dialog `Unsaved Changes` (severity warning) tampil
26. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
27. Verifikasi tombol `[Cancel]` tampil pada dialog
28. Verifikasi tombol `[Leave]` tampil pada dialog
29. Klik `[Leave]`
30. Verifikasi modal Create tertutup
31. Verifikasi tabel menampilkan 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury)
32. Verifikasi Division `Draft Division` tidak ada di tabel
33. Verifikasi Create Division (`POST /v2/iam/divisions`) tidak terpanggil

## Notes

- Mode: mock. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 70, 68, 71, 69 (urutan TC sumber 68, 69, 70, 71). Alasan: TC-GS-DIV-69 (`[Leave]`) menutup form dan membuang input sehingga ditaruh paling akhir (prinsip 6 konvensi: kasus menutup form di akhir); ketiga TC lain memakai satu pembukaan form yang sama. Hanya satu kali `[+ Division]` dibuka untuk empat TC.
- Langkah penghubung: tidak ada; seluruh langkah tanpa `Verifikasi` (langkah 1, 2, 3, 8, 11, 16, 20, 24, dan 29) adalah aksi TC sumber.
- Langkah 31 sampai 33 mengasersi "Draft Division tidak dibuat": langkah 31 adalah anchor positif (tabel sudah dimuat), langkah 32 lewat tabel (respons list mock tidak memuatnya, sehingga langkah itu bermakna sebagai pelengkap) dan langkah 33 lewat tidak terpanggilnya Create Division (Prerequisites), yang menjadi bukti utama.
- Temuan untuk QA: TC-GS-DIV-70 Expected d tidak menyatakan dialog tertutup sesudah `[Cancel]`; spec hanya mengasersi modal terbuka dan input dipertahankan (langkah 9 dan 10), sedangkan penutupan dialog diasersi pada TC-GS-DIV-68 (langkah 17).
- Label tombol dialog `Unsaved Changes` adalah `[Cancel]` dan `[Leave]` sesuai NC-12 dan `prd-conventions.md` §24.1c.
