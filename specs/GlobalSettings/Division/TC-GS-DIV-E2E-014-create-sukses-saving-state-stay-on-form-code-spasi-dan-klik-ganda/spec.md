---
id: TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda
title: "Create Division Sukses: Saving State, Stay on Form, Code Spasi Saja, dan Klik Ganda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-33
  - TC-GS-DIV-49
  - TC-GS-DIV-65
  - TC-GS-DIV-66
  - TC-GS-DIV-78
coverage:
  web: automated
---

# Create Division Sukses: Saving State, Stay on Form, Code Spasi Saja, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata). Kasus saving state (TC-GS-DIV-33) memakai intercept parsial di atas backend nyata.
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury) sebagai latar tabel; tidak diubah spec ini.
- Data dinamis (dibuat lewat UI oleh spec ini; Name memakai suffix per run `{runId}-014`, Code memakai nilai literal TC):
  - D-11: Name `Investor Relations {runId}-014`, Code `INV` (TC-GS-DIV-66).
  - Name `Procurement Team {runId}-014`, Code dikosongkan sehingga di-generate otomatis (TC-GS-DIV-33; hasil Code tidak diasersi).
  - D-09: Name `Quality Control` (literal tanpa suffix karena Code `QC` hasil auto-generate bergantung pada dua token Name), Code berisi 3 spasi (TC-GS-DIV-49).
  - D-12: Name `Treasury Operations {runId}-014`, Code `TRO` (TC-GS-DIV-78).
  - D-10: Name `Public Relations {runId}-014`, Code `PR` (TC-GS-DIV-65).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: hapus lewat API sisa Division run sebelumnya yang bernama memuat `-014` atau bernama persis `Quality Control`, supaya Code literal (`INV`, `TRO`, `PR`, `QC`) tidak bentrok sebagai duplikat.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua Division milik spec ini (bernama memuat `{runId}-014` dan `Quality Control`) bila masih ada, serta lepas intercept bila masih terpasang.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons Create Division sampai intercept dilepas di langkah 23 (TC-GS-DIV-33; nilai delay 3 detik pada data uji TC hanya contoh delay, sehingga tujuh asersi Saving tidak terikat batas 3 detik); klik ganda cepat pada `[Submit]` (TC-GS-DIV-78); hover pada tombol dan pembacaan background hover; pembacaan fokus keyboard; pembacaan state disabled; pembacaan teks sel tabel; Search pada tabel.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah (intercept dilepas di langkah 23 dan di hook `after`).

## Test Steps

### TC-GS-DIV-66: Submit Create dengan Stay checked mereset form dan tetap terbuka

1. Klik `[+ Division]`
2. Centang `Stay on this form after submitting`
3. Isi Division Name `Investor Relations {runId}-014` dan Code `INV` (D-11)
4. Klik `[Submit]`
5. Verifikasi toast sukses: `Success, division has been created.`
6. Verifikasi modal tetap terbuka
7. Verifikasi Division Name kosong
8. Verifikasi Code kosong
9. Verifikasi fokus kembali ke Division Name
10. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang

### TC-GS-DIV-33: Tombol Submit masuk Saving state dan seluruh kontrol form disabled

11. Pasang intercept yang menahan respons Create Division sampai intercept dilepas
12. Isi Division Name `Procurement Team {runId}-014`
13. Hover `[Submit]`
14. Verifikasi hover `[Submit]` menampilkan background success hover
15. Klik `[Submit]`
16. Verifikasi `[Submit]` menampilkan spinner
17. Verifikasi `[Submit]` disabled
18. Verifikasi field Division Name ikut disabled
19. Verifikasi field Code ikut disabled
20. Verifikasi checkbox `Stay on this form after submitting` ikut disabled
21. Verifikasi `[Clear Field]` ikut disabled
22. Verifikasi icon `[✕]` ikut disabled
23. Lepas intercept penahan respons
24. Tunggu aksi selesai (field Division Name kembali kosong dan `[Submit]` aktif)

### TC-GS-DIV-49: Code berisi spasi saja dianggap kosong dan di-generate otomatis

25. Isi Division Name `Quality Control` dan Code dengan 3 spasi (D-09)
26. Verifikasi tidak ada error pada Code
27. Klik `[Submit]`
28. Verifikasi toast sukses: `Success, division has been created.`

### TC-GS-DIV-78: Klik ganda Submit hanya membuat satu Division

29. Isi Division Name `Treasury Operations {runId}-014` dan Code `TRO` (D-12)
30. Klik `[Submit]` dua kali cepat
31. Verifikasi `[Submit]` disabled setelah klik pertama
32. Tunggu aksi selesai (field Division Name kembali kosong dan `[Submit]` aktif)
33. Verifikasi tidak ada error duplicate (`Division Name already exists` dan `Code already exists` tidak tampil)

### TC-GS-DIV-65: Submit Create dengan Stay unchecked menutup modal

34. Lepas centang `Stay on this form after submitting`
35. Isi Division Name `Public Relations {runId}-014` dan Code `PR` (D-10)
36. Klik `[Submit]`
37. Verifikasi toast sukses: `Success, division has been created.`
38. Verifikasi modal Create Division tertutup

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-DIV-65, 78, 49)

39. Ketik Search `{runId}-014`, tekan Enter
40. Verifikasi baris `Public Relations {runId}-014` tampil di tabel (TC-GS-DIV-65)
41. Verifikasi hanya 1 baris `Treasury Operations {runId}-014` tampil di tabel (TC-GS-DIV-78)
42. Ganti isi kotak search dengan `Quality Control`, tekan Enter
43. Verifikasi tabel menampilkan Code `QC` hasil auto-generate pada baris `Quality Control` (TC-GS-DIV-49)
44. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (intercept parsial untuk TC-GS-DIV-33). Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 66, 33, 49, 78, lalu 65 (urutan TC sumber 33, 49, 65, 66, 78). Alasan: keempat TC pertama berbagi satu sesi modal dengan Stay tercentang (prinsip 8 konvensi), sedangkan TC-GS-DIV-65 mengharuskan Stay tidak tercentang sehingga Submit menutup form dan menjadi kejadian menutup form di akhir (prinsip 6 konvensi). Hanya satu kali `[+ Division]` dibuka. TC-GS-DIV-66 dijalankan lebih dulu karena memeriksa perilaku Stay pada Submit pertama.
- Asersi "tabel menampilkan ..." milik TC-GS-DIV-65, TC-GS-DIV-78, dan TC-GS-DIV-49 ditaruh sesudah form ditutup (langkah 39 sampai 43) karena tabel berada di belakang modal selama Stay tercentang; toast dicek langsung sesudah tiap Submit. Satu Search `{runId}-014` menampilkan empat baris bersuffix (kurang dari 10 baris, satu halaman).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 34 (mengatur mode sesi modal Stay, bukan asersi TC), langkah 23 (melepas intercept untuk TC-GS-DIV-33), langkah 24 dan 32 (menunggu aksi selesai sebelum aksi berikutnya yang ikut disabled selama Saving), langkah 39 dan 42 (Search agar baris target tampil di halaman aktif), dan langkah 44 (mengosongkan Search).
- Name `Quality Control` literal tanpa suffix karena asersi Code `QC` bergantung pada dua token Name (bagian 5 konvensi, S-12); dibersihkan lewat API di hook `before` dan `after`.
- Spec melewati sekitar 35 langkah (44 langkah) karena lima TC Create sukses berkelas harness sama (aksi sukses) dan berbagi satu sesi modal Stay; TC-GS-DIV-33 sendiri 14 langkah akibat butir Expected yang dipecah per klausa (S-01). Tiap blok memakai Name sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemecahan hanya menambah login, hook, dan pembukaan form.
- Temuan untuk QA:
  - TC-GS-DIV-33 tidak menyatakan hasil sesudah respons kembali (toast, state form); Division `Procurement Team {runId}-014` tetap tercipta dan dibersihkan lewat API, dan spec tidak mengasersi toast-nya. Langkah 2 TC (menahan respons) juga tidak menyebut Stay; spec menjalankannya dengan Stay tercentang.
  - TC-GS-DIV-78 Expected a (`[Submit]` disabled setelah klik pertama) sulit teramati pada klik ganda cepat tanpa penahanan respons; TC tidak menyebut penahanan respons, spec mengikuti TC.
  - TC-GS-DIV-78 Expected b ("tidak ada error duplicate") tidak menyebut teks error; langkah 33 memakai teks error duplikat `Division Name already exists` dan `Code already exists` dari TC-GS-DIV-40 dan TC-GS-DIV-48.
