---
id: TC-AC-DN-E2E-045-create-validasi-emoji
title: "Create Device Name: Emoji Diketik, Ditempel, dan Lolos Filter FE"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-97
  - TC-AC-DN-98
  - TC-AC-DN-99
coverage:
  web: automated
---

# Create Device Name: Emoji Diketik, Ditempel, dan Lolos Filter FE

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`).
- Data uji teks: `Gate😊` (diketik, TC-AC-DN-97) dan `Kamera🔥Pintu` (ditempel, TC-AC-DN-98) tidak pernah tersimpan sehingga tidak bersuffix; Device Name TC-AC-DN-99 `Gate Antenna Baru {runId}-045` ditambah karakter 😊 yang disisipkan lewat DOM.
- Kemampuan teknis: menyalin teks ke clipboard dan menempelnya ke field; menyisipkan karakter langsung ke nilai input lewat console browser sehingga melewati filter keystroke dan paste (TC-AC-DN-99); disediakan tim FE.
- Tidak ada record yang dibuat (semua [Submit] ditolak), sehingga tidak ada cleanup. State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-97: Emoji yang diketik diblok

1. Klik tombol `+ Device Name` pada toolbar
2. Klik field Device Name lalu ketik "Gate😊" dengan keyboard
3. Verifikasi field Device Name hanya berisi `Gate` dan karakter emoji tidak masuk ke field
4. Verifikasi tidak ada pesan error pada field Device Name

### TC-AC-DN-98: Emoji yang ditempel diblok

5. Klik `[Clear Field]`
6. Salin teks "Kamera🔥Pintu" ke clipboard
7. Tempel (paste) ke field Device Name
8. Verifikasi field Device Name hanya berisi `KameraPintu` dan karakter emoji tidak masuk ke field
9. Verifikasi tidak ada pesan error pada field Device Name

### TC-AC-DN-99: Emoji yang lolos filter FE ditolak saat Submit

10. Klik `[Clear Field]`
11. Ketik `Gate Antenna Baru {runId}-045` pada field Device Name
12. Lewat console browser, sisipkan karakter 😊 langsung ke nilai input Device Name sehingga melewati filter keystroke dan paste
13. Klik field Measurement lalu pilih `Unit`
14. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
15. Klik `[Submit]`
16. Verifikasi error inline "Device name contains invalid characters" muncul di bawah field Device Name
17. Verifikasi popup form tetap terbuka
18. Verifikasi tidak ada toast sukses
19. Klik `[Clear Field]`
20. Klik icon close `[✕]` pada popup

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. TC-AC-DN-97 dan TC-AC-DN-98 bertanda FE Test "UI Only"; TC-AC-DN-99 "Need API" (penolakan karakter tidak valid pada Submit).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 5 dan 10 (`[Clear Field]` mengosongkan isian TC sebelumnya, S-09), langkah 19 dan 20 (pemulihan form dirty lalu menutup form kosong tanpa dialog `Unsaved Changes`).
- Pemicu karakter emoji lewat console browser (langkah 12) mengikuti langkah TC-AC-DN-99 dan hanya pemicu state; yang diasersi adalah error dari penolakan saat Submit (kelas harness `-`, bukan request langsung ke server).
- Temuan untuk QA:
  - Post Condition "Tidak ada record baru tersimpan" (TC-AC-DN-99) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-AC-DN-97 dan TC-AC-DN-98 menyatakan "tidak ada pesan error" tanpa menyebut timing pengamatan; diasersi segera setelah ketikan atau paste.
