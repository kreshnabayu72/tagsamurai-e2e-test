---
id: TC-FA-FAAL-E2E-017-guided-tooltip-navigasi-dan-keyboard
title: "Guided Tooltip: Navigasi Back/Next/Done/Skip dan Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-200
  - TC-FA-FAAL-202
coverage:
  web: automated
---

# Guided Tooltip: Navigasi Back/Next/Done/Skip dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control tanpa flag Guided Tooltip (Pre-setup #4), `totalControlNewGuide_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TCNEWGUIDE_PASSWORD`.
- Login akun aktor pertama (Pre-setup #4) di hook `before` spec ini. Pengecualian atas `suite.md`: spec Guided Tooltip dikecualikan dari hook suite flag dan precondition kedua TC adalah Fixed Asset > Dashboard, sehingga hook `beforeEach` membuka Fixed Asset > Dashboard (bukan Activity Log) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Flag Guided Tooltip halaman Activity Log (`guided_tooltip_seen_fa-activity-log`): akun #4 direset ke belum diset oleh langkah penghubung di awal tiap blok TC (kemampuan reset flag disediakan tim FE/BE; mekanisme tidak tertulis di TC) dan dipulihkan ke belum diset di hook `after`.
- Kemampuan teknis disediakan tim FE: pembacaan nilai flag `guided_tooltip_seen_fa-activity-log` untuk Expected TC-FA-FAAL-200 butir d (tanpa endpoint karangan, S-13).
- Env var `FA_TCNEWGUIDE_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: spec tidak memakai baris log tertentu; tabel boleh berisi log apa pun.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas akun Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-200: Guided Tooltip navigasi Back, Next, Done, dan Skip

1. Reset flag Guided Tooltip halaman Activity Log akun #4 menjadi belum diset
2. Buka Reports & Logs > Activity Log pertama kali
3. Verifikasi step 1: tombol `[Back]` tidak tampil
4. Klik `[Next]` hingga step 3
5. Verifikasi step 3: menampilkan `[Done]` sebagai pengganti `[Next]`
6. Klik `[Back]`
7. Verifikasi `[Back]` kembali ke step 2
8. Klik `[Next]`
9. Klik `[Done]`
10. Verifikasi `[Done]` menutup walkthrough
11. Verifikasi flag `guided_tooltip_seen_fa-activity-log` bernilai true
12. Buka ulang walkthrough lewat tombol `[?]` di kanan Breadcrumb
13. Klik overlay gelap
14. Verifikasi klik overlay gelap menutup walkthrough sama seperti `[Skip]`

### TC-FA-FAAL-202: Guided Tooltip navigasi keyboard

15. Reset flag Guided Tooltip halaman Activity Log akun #4 menjadi belum diset
16. Buka Reports & Logs > Activity Log pertama kali
17. Verifikasi kotak tooltip menerima fokus keyboard
18. Tekan `Enter`
19. Verifikasi `Enter` ke step berikutnya
20. Tekan `←`
21. Verifikasi `←` ke step sebelumnya
22. Tekan `→`
23. Verifikasi `→` ke step berikutnya
24. Tekan `Esc`
25. Verifikasi `Esc` menutup walkthrough seperti Skip

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAL-197, 198, 199, dan 201 ada di spec 016.
- Langkah penghubung (S-03): langkah 1 dan 15 (reset flag akun #4 sebelum tiap TC, sesuai catatan Pre-setup TC bahwa flag #4 dipulihkan sebelum tiap TC yang memakainya), dan langkah 12 (membuka ulang walkthrough lewat `[?]` yang diminta TC langkah 5).
- Asersi state sementara (bagian 8b butir 5): fokus keyboard (langkah 17) diasersi sebelum tombol pertama ditekan; setiap tombol keyboard diikuti `Verifikasi` sebelum tombol berikutnya.
- Langkah 11: Expected TC-FA-FAAL-200 butir d memuat dua klausa ("menutup walkthrough" dan "flag true") yang dipecah (S-01); pembacaan flag disediakan tim FE/BE.
- Ukuran spec 25 langkah, di bawah ambang.
- Temuan untuk QA:
  - TC-FA-FAAL-200 dan 202 tidak menyebut env var password dan cara mereset flag; nama env var diusulkan dari butir "Env var" di `suite.md` dan mekanisme reset disediakan tim FE/BE.
  - TC-FA-FAAL-200 langkah 5 ("Buka ulang lewat `[?]`, klik overlay gelap") dan Expected butir e tidak menyebut apakah klik overlay mengubah nilai flag; spec hanya mengasersi penutupan walkthrough.
