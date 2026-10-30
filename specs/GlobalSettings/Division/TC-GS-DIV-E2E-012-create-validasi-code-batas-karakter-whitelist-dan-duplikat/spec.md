---
id: TC-GS-DIV-E2E-012-create-validasi-code-batas-karakter-whitelist-dan-duplikat
title: "Create Division: Validasi Code (16 Karakter, Simbol Terlarang, Duplikat)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-45
  - TC-GS-DIV-46
  - TC-GS-DIV-48
coverage:
  web: automated
---

# Create Division: Validasi Code (16 Karakter, Simbol Terlarang, Duplikat)

## Prerequisites

- Mode: FE+BE (backend nyata; TC-GS-DIV-48 butuh pengecekan keunikan Code ke backend).
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec): Division `Finance` dengan Code `FIN` sebagai Code yang sudah ada untuk TC-GS-DIV-48.
- Data uji: semua nilai hanya diketik dan seluruh submit diblokir, sehingga tidak ada Division yang dibuat dan tidak ada seeding. Nilai uji: Code 16 karakter `CODE-15-CHARS-AX` (TC-GS-DIV-45), Code `FIN@1` (TC-GS-DIV-46), Division Name `Financial Planning` dan Code `fin` (TC-GS-DIV-48).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `before`: mencatat jumlah Division sebagai baseline (dipakai langkah 15).
- Hook `afterEach`: tutup modal Create yang masih terbuka dan dirty lewat `✕`, lalu klik `[Leave]` pada dialog `Unsaved Changes`, kembali ke layar Division (cadangan bila langkah 16 sampai 18 tidak tercapai).
- Cleanup (hook `after`): bila ada Division tidak terduga yang terbentuk dengan Name `Financial Planning`, hapus lewat API; tidak berasumsi langkah UI berhasil.
- Kemampuan teknis: pengetikan karakter demi karakter; penantian debounce ±500 ms; pembacaan nilai field Code dan panjang nilainya; pembacaan jumlah Division lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control, Sari Dewi).

## Test Steps

### TC-GS-DIV-45: Code 16 karakter diterima input dan menampilkan error inline

1. Klik `[+ Division]`
2. Ketik 16 karakter `CODE-15-CHARS-AX` pada field Code
3. Verifikasi input menerima seluruh 16 karakter (panjang nilai field Code 16 karakter)
4. Verifikasi error inline `Max. 15 characters` muncul langsung saat melebihi 15 karakter

### TC-GS-DIV-46: Code dengan karakter di luar whitelist menampilkan error inline

5. Klik `[Clear Field]`
6. Ketik `FIN@1` pada field Code
7. Verifikasi error inline `Code contains invalid characters` muncul langsung saat mengetik

### TC-GS-DIV-48: Code duplikat tanpa membedakan huruf besar kecil menampilkan error setelah debounce

8. Klik `[Clear Field]`
9. Isi Division Name `Financial Planning`
10. Ketik `fin` pada field Code
11. Verifikasi Code berubah menjadi `FIN` saat mengetik
12. Berhenti mengetik ±500 ms
13. Verifikasi error inline `Code already exists` muncul setelah debounce
14. Klik `[Submit]`
15. Verifikasi record tidak dibuat: jumlah Division lewat API sama dengan baseline

### Tutup form dirty

16. Klik `✕` untuk menutup form yang masih dirty
17. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
18. Klik `[Leave]` pada dialog `Unsaved Changes`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh validasi memakai satu pembukaan form (prinsip 3, 6, dan 7 konvensi), dalam urutan TC sumber (45, 46, 48). Form ditutup di akhir spec (langkah 16 sampai 18). Pengecekan "tidak ada record" dilakukan sekali di langkah 15 lewat API karena tabel tertutup modal; jumlah dibandingkan dengan baseline dari hook `before` sehingga mencakup seluruh submit sebelumnya.
- Langkah 14 dan 15 (TC-GS-DIV-48) menambahkan submit yang diblokir sesuai prinsip 7 konvensi; TC sumber hanya meminta error inline. Nilai Code `FIN` yang duplikat masih tampil pada field saat submit, sehingga submit diblokir oleh validasi Code.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 8 (`[Clear Field]` mengosongkan field sebelum nilai uji berikutnya), langkah 12 (jeda debounce ±500 ms sesudah mengetik, supaya langkah 11 mengamati keadaan sebelum debounce), serta langkah 16 dan 18 (menutup form dirty lewat `✕` dan `[Leave]`; langkah 17 memverifikasi dialog `Unsaved Changes` sesuai S-08, bukan Expected TC).
- Langkah 9 (mengisi Division Name `Financial Planning`) adalah langkah 2 TC-GS-DIV-48 dan tidak ada pada TC-GS-DIV-45 dan TC-GS-DIV-46 (Division Name dibiarkan kosong pada kedua TC itu).
- Temuan untuk QA: TC-GS-DIV-45 dan TC-GS-DIV-46 tidak memuat langkah submit; langkah 14 dan 15 adalah tambahan prinsip 7 konvensi (bukan Expected TC).
