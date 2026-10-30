---
id: TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat
title: "Edit Division: Validasi Name (Kosong, Spasi, 121 Karakter, Emoji, Duplikat, Nilai Sendiri)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-83
  - TC-GS-DIV-84
  - TC-GS-DIV-87
  - TC-GS-DIV-88
  - TC-GS-DIV-89
  - TC-GS-DIV-90
  - TC-GS-DIV-91
  - TC-GS-DIV-92
coverage:
  web: automated
---

# Edit Division: Validasi Name (Kosong, Spasi, 121 Karakter, Emoji, Duplikat, Nilai Sendiri)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var), lalu sesi dipakai sepanjang spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (data environment tetap, hanya dibaca sebagai nilai duplikat; tidak diubah): Division `Finance` (Code `FIN`, bebas relasi). Fixture belum ada; tim FE menyiapkan `fixtures/division.json` untuk identitas data ini.
- Data dinamis (seeding Division lewat API di hook `before`; target Edit milik spec ini, pengganti `Accounting` dan `Audit` pada TC sumber agar Population D-02 tidak ikut dibutuhkan): `Audit {runId}-024` dengan Code `EDT24` (Code literal karena tidak diberi suffix per run). Seluruh kasus berakhir pada Save yang diblokir atau tanpa Save dan form ditutup lewat `[Leave]`, sehingga Division ini tidak pernah berubah.
- Nilai input uji dibangun atau diketik langsung oleh langkah: `Audit 😀` (TC-GS-DIV-88), 121 karakter `Divisions of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APACs` (TC-GS-DIV-87), 3 spasi (TC-GS-DIV-84), `finance` dan `Finance` (TC-GS-DIV-89 dan 90), dan versi huruf besar seluruhnya dari `Audit {runId}-024` (TC-GS-DIV-92).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API Division `Audit {runId}-024` dan Division berkode `EDT24` bila masih ada. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: input keystroke emoji; mengetik string 121 karakter; menunggu debounce ±500 ms; mengklik `[Save]` sebelum debounce selesai; membaca border field (`severity="danger"`); menunggu respons `POST /v2/iam/divisions/check-availability` selesai (dipakai sebelum asersi tidak ada error duplikat).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-88: Edit Division Name berisi emoji menampilkan error inline

1. Ketik Search `Audit {runId}-024`, tekan Enter
2. Buka row action baris `Audit {runId}-024` lalu klik `Edit`
3. Ganti isi Division Name dengan `Audit 😀`
4. Verifikasi error inline `Division Name contains invalid characters` tampil langsung saat mengetik
5. Klik `[Save]`
6. Verifikasi tidak ada toast sukses
7. Verifikasi Save diblokir: modal Edit tetap terbuka

### TC-GS-DIV-87: Edit Division Name 121 karakter diterima input dan menampilkan error inline

8. Ganti isi Division Name dengan string 121 karakter (`Divisions of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APACs`)
9. Verifikasi input menerima seluruh 121 karakter
10. Verifikasi error inline `Max. 120 characters` tampil langsung saat melebihi batas
11. Klik `[Save]`
12. Verifikasi tidak ada toast sukses
13. Verifikasi Save diblokir: modal Edit tetap terbuka

### TC-GS-DIV-83: Save Edit dengan Division Name dikosongkan

14. Kosongkan Division Name
15. Klik `[Save]`
16. Verifikasi perubahan tidak tersimpan (tidak ada toast sukses)
17. Verifikasi pesan error inline `Division Name must not be empty`
18. Verifikasi field Division Name berborder `severity="danger"`
19. Verifikasi modal Edit tetap terbuka

### TC-GS-DIV-84: Save Edit dengan Division Name hanya spasi

20. Ganti isi Division Name dengan 3 spasi
21. Klik `[Save]`
22. Verifikasi tidak ada toast sukses
23. Verifikasi Name diperlakukan kosong: pesan inline `Division Name must not be empty`
24. Verifikasi perubahan tidak tersimpan: modal Edit tetap terbuka

### TC-GS-DIV-89: Edit Division Name menjadi duplikat Division lain menampilkan error

25. Ganti isi Division Name dengan `finance`
26. Tunggu ±500 ms (debounce pengecekan keunikan)
27. Verifikasi error inline `Division Name already exists` tampil setelah debounce
28. Klik `[Save]`
29. Verifikasi tidak ada toast sukses
30. Verifikasi `[Save]` tidak menyimpan perubahan ke nilai duplikat: modal Edit tetap terbuka

### TC-GS-DIV-91: Mengetik ulang Division Name yang sama dengan nilai sendiri tidak menampilkan error duplicate

31. Hapus isi Division Name, lalu ketik ulang `Audit {runId}-024`
32. Tunggu ±500 ms (debounce pengecekan keunikan)
33. Tunggu respons check-availability selesai
34. Verifikasi tidak ada error duplicate terhadap diri sendiri pada Division Name

### TC-GS-DIV-92: Mengubah Division Name hanya pada huruf besar kecil tidak dianggap duplikat terhadap diri sendiri

35. Ganti isi Division Name dengan versi huruf besar seluruhnya dari `Audit {runId}-024`
36. Tunggu ±500 ms (debounce pengecekan keunikan)
37. Tunggu respons check-availability selesai
38. Verifikasi tidak ada error `Division Name already exists` terhadap record itu sendiri

### TC-GS-DIV-90: Save langsung dengan Division Name duplikat sebelum debounce selesai ditolak

39. Ganti isi Division Name dengan `Finance`
40. Klik `[Save]` segera sebelum 500 ms berlalu
41. Verifikasi perubahan tidak tersimpan (tidak ada toast sukses)
42. Verifikasi error inline `Division Name already exists` tampil
43. Verifikasi modal Edit tetap terbuka
44. Verifikasi input `Finance` dipertahankan
45. Klik `✕` di header modal Edit
46. Verifikasi dialog `Unsaved Changes` tampil
47. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
48. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
49. Klik `[Leave]`
50. Verifikasi Name `Audit {runId}-024` pada baris di tabel tidak berubah

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-83, 84, 87, 88, 89, 90, 91, 92). Mode: FE+BE. Kelas harness: validasi diblokir.
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC berbeda dari urutan nomor TC sumber: kasus yang berhenti pada error saat mengetik lebih dulu (TC-88, TC-87), lalu validasi Save diblokir (TC-83, TC-84, TC-89), kemudian kasus nilai sendiri (TC-91, TC-92) yang diletakkan sesudah TC-89 supaya hilangnya error duplikat teramati, dan TC-90 terakhir karena Save dilakukan sebelum debounce selesai dan form berakhir dalam keadaan dirty yang ditutup lewat `[Leave]` (prinsip 6). Seluruh TC memakai satu pembukaan modal Edit (satu kejadian menutup form).
- Langkah 5 sampai 7 dan 11 sampai 13 adalah penerapan prinsip 7 untuk TC-GS-DIV-88 dan TC-GS-DIV-87 (tiap validasi diakhiri submit yang diblokir); Langkah Uji TC sumber hanya berhenti pada mengetik. Langkah 16 dan 19, 22 dan 24, 29 dan 30, 41 sampai 44, serta 50 memetakan Expected "perubahan tidak tersimpan" pada TC-GS-DIV-83, 84, 89, dan 90 (langkah 50 memeriksa Division tidak berubah di tabel).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari target Edit), langkah 26, 32, dan 36 (menunggu debounce) serta langkah 33 dan 37 (menunggu respons check-availability selesai sebelum asersi tidak ada error), dan langkah 45 sampai 49 (menutup form dirty lewat `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]`; teks dan tombol dialog dari TC-GS-DIV-107 dan NC-12).
- Target Edit memakai Division milik spec (`Audit {runId}-024`) sebagai pengganti `Accounting` dan `Audit` pada TC sumber. Division `Finance` Pre-setup hanya menjadi nilai duplikat dan tidak diubah.
- Spec melewati sekitar 35 langkah (50 langkah) karena memuat delapan validasi Name pada satu modal Edit yang sama; seluruhnya satu kelas harness (validasi diblokir) dengan satu pembukaan form yang dipakai berurutan, sehingga tiap blok melanjutkan state field dari blok sebelumnya dan memecahnya hanya menambah pembukaan form dan login.
- Temuan untuk QA:
  - TC-GS-DIV-87 mengambil 121 karakter literal yang berakhir `APACs`; spec memakai nilai itu persis.
  - Post Condition TC-GS-DIV-83, 84, 90 ("Name tidak berubah") tidak punya langkah observasi; asersi di langkah 50 hanya mengacu ke Expected "perubahan tidak tersimpan".
  - TC-GS-DIV-91 dan 92 tidak menyebut Save; keduanya berhenti pada tidak adanya error.
