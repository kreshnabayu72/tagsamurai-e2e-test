---
id: TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use
title: "Absence Log: Edit Tanpa Perubahan dan Division In-Use Dilewati Tidak Menghasilkan Entri"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-240
  - TC-GS-DIV-244
  - TC-GS-DIV-300
  - TC-GS-DIV-99
  - TC-GS-DIV-100
  - TC-GS-DIV-288
coverage:
  web: automated
---

# Absence Log: Edit Tanpa Perubahan dan Division In-Use Dilewati Tidak Menghasilkan Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini karena aksinya No-Op atau dilewati; Last Updated tidak berubah): `Human Resources` (Code `HR`, in-use: Login User aktif Budi Santoso), target Edit No-Op TC-GS-DIV-99 dan Division yang dilewati pada TC-GS-DIV-244.
- Data dinamis (milik spec ini, bersuffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before`:
  - `Accounting {runId}-067`: target Edit No-Op TC-GS-DIV-100 (pengganti `Accounting` Population D-02 karena tidak diubah dan tidak dihapus).
  - `Log Gen 2 {runId}-067`: target Edit No-Op TC-GS-DIV-240.
  - `Syslog NoOp {runId}-067`: target Edit No-Op TC-GS-DIV-300.
  - `Skip Free {runId}-067`: Division bebas relasi, ikut dicentang bersama `Human Resources` pada Bulk Delete TC-GS-DIV-244 (pengganti `Information Technology`).
  - `Information Technology` dengan Code `IT` (Population D-02): bernama literal tanpa suffix karena kandidat auto-generate `IT` harus identik dengan Code sendiri pada TC-GS-DIV-288 (bagian 5 konvensi, S-12). Di-seed idempotent lewat API di hook `before` (dilewati bila sudah ada); cleanup hanya menghapusnya bila dibuat spec ini; suite berjalan serial (S-12). Hook `before` juga menghapus lewat API sisa Division bersuffix `-067` dari run lama (bukan berdasarkan kode).
  - Kode Division bersuffix di atas dibiarkan kosong saat seeding (di-generate otomatis) karena tidak diasersi.
- Kemampuan teknis: seeding Division lewat API dan penghapusan Division lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Baseline log: setelah hook `before` selesai dan sebelum aksi pertama, spec mencatat jumlah total entri tiap surface (`{nChangelog}`, `{nActivity}`, `{nSystem}`) pada Modal Changelog, Activity Log, dan Tab System Log Sari Dewi. Entri hasil seeding hook `before` sudah termasuk dalam baseline sehingga tidak ikut dihitung sebagai entri baru.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division bersuffix `{runId}-067` yang masih ada dan `Information Technology` bila dibuat spec ini; pulihkan page size tabel Division ke 10 serta Search dan seleksi tabel ke default.
- Tabel Division berurut A-Z dengan page size 10 dan memuat lebih dari satu halaman: `Human Resources` dan `Skip Free {runId}-067` tidak dijamin tampil bersamaan di halaman 1, sehingga pencentangan keduanya memakai page size 50 (opsi paginasi tabel).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Tidak ada state global yang diubah.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- TC-GS-DIV-240, 244, 300, 99, 100, 288: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### Baseline log sebelum aksi

1. Buka Modal Changelog, catat jumlah total entri Changelog sebagai baseline `{nChangelog}`
2. Tutup Modal Changelog, buka Global Settings > Activity Log, catat jumlah total entri Activity Log sebagai baseline `{nActivity}`
3. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, catat jumlah total entri System Log sebagai baseline `{nSystem}`

### TC-GS-DIV-99: Edit dengan Code dikosongkan yang hasil generate identik dengan Code sendiri tidak berubah

4. Buka Global Settings > User > Division, ketik Search `Human Resources`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit
5. Kosongkan Code
6. Klik [Save]
7. Tunggu aksi selesai (modal Edit tertutup)

### TC-GS-DIV-288: Edit dengan Code berisi spasi saja dianggap kosong dan di-generate otomatis

8. Ganti isi kotak search tabel Division dengan `Information Technology`, tekan Enter, klik `⋯` pada baris tersebut > Edit
9. Ganti Code dengan 3 spasi
10. Klik [Save]
11. Tunggu aksi selesai (modal Edit tertutup)

### TC-GS-DIV-100: Save Edit tanpa perubahan data menutup modal dengan toast netral

12. Ganti isi kotak search tabel Division dengan `Accounting {runId}-067`, tekan Enter, klik `⋯` pada baris tersebut > Edit
13. Klik [Save] tanpa mengubah field apa pun
14. Tunggu aksi selesai (modal Edit tertutup)

### TC-GS-DIV-240: Edit tanpa perubahan tidak mencatat entri apa pun

15. Ganti isi kotak search tabel Division dengan `Log Gen 2 {runId}-067`, tekan Enter, klik `⋯` pada baris tersebut > Edit
16. Klik [Save] tanpa perubahan
17. Verifikasi toast netral: "No changes to save."

### TC-GS-DIV-300: Edit tanpa perubahan tidak menulis entri di Tab System Log aktor

18. Ganti isi kotak search tabel Division dengan `Syslog NoOp {runId}-067`, tekan Enter, klik `⋯` pada baris tersebut > Edit
19. Klik [Save] tanpa perubahan
20. Verifikasi toast netral: "No changes to save."

### TC-GS-DIV-244: Division yang di-skip karena in-use tidak menghasilkan entri log

21. Ubah page size tabel Division menjadi 50, klik `(←)` pada kotak Search, centang baris `Human Resources` dan `Skip Free {runId}-067`
22. Klik aksi [Delete] pada Bulk Action Bar
23. Klik [Continue] pada dialog Delete Division
24. Tunggu aksi selesai (dialog Delete Division tertutup)
25. Ubah page size tabel Division kembali menjadi 10

### Pemeriksaan log di tiga surface (Expected Result log TC-GS-DIV-99, 288, 100, 240, 300, 244)

26. Buka Modal Changelog
27. Verifikasi jumlah total entri Changelog bertambah tepat 1 dari baseline `{nChangelog}`, yaitu entri baru Action `Delete`, Division Name `Skip Free {runId}-067`, Field `Division Name`, Old Value `Skip Free {runId}-067`, New Value `—`
28. Verifikasi entri baru Changelog sejak baseline `{nChangelog}` tidak memuat entri untuk `Human Resources`, `Information Technology`, `Accounting {runId}-067`, `Log Gen 2 {runId}-067`, dan `Syslog NoOp {runId}-067`
29. Tutup Modal Changelog, buka Global Settings > Activity Log
30. Verifikasi jumlah total entri Activity Log bertambah tepat 1 dari baseline `{nActivity}`, yaitu entri baru Action `Delete`, Object `Division`, Name `Skip Free {runId}-067`
31. Verifikasi entri baru Activity Log sejak baseline `{nActivity}` tidak memuat entri untuk `Human Resources`, `Information Technology`, `Accounting {runId}-067`, `Log Gen 2 {runId}-067`, dan `Syslog NoOp {runId}-067`
32. Buka Global Settings > User > Detail Sari Dewi > Tab System Log
33. Verifikasi jumlah total entri System Log Sari Dewi bertambah tepat 1 dari baseline `{nSystem}`, yaitu entri baru Action `Delete`, Object `Division`, Name `Skip Free {runId}-067`
34. Verifikasi entri baru System Log Sari Dewi sejak baseline `{nSystem}` tidak memuat entri untuk `Human Resources`, `Information Technology`, `Accounting {runId}-067`, `Log Gen 2 {runId}-067`, dan `Syslog NoOp {runId}-067`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Spec ini kelas g (asersi absence).
- Pembagian TC lintas spec: TC-GS-DIV-99, 100, dan 288 terbelah; aksi dan Expected Result selain "tidak ada entri log" (toast netral, modal tertutup, Code tetap, dialog Unsaved Changes, pesan error) ada di spec `TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op`. Spec ini memuat aksi pemicu (langkah 4 sampai 6, 8 sampai 10, dan 12 sampai 13) tanpa `Verifikasi` fungsional, serta asersi tidak ada entri log baru (langkah 28, 31, dan 34) dengan baseline jumlah total entri dan anchor positif.
- Urutan TC di spec: 99, 288, 100, 240, 300 (semua Edit No-Op, tidak mengubah data), lalu 244 (Bulk Delete) paling akhir (prinsip 5) karena menghapus `Skip Free {runId}-067`. Pemeriksaan log di tiga surface dilakukan sekali sesudah semua aksi dengan satu baseline jumlah total entri per surface, sehingga satu rangkaian membuktikan kelima aksi No-Op dan Division in-use yang dilewati tidak menulis entri.
- Anchor positif (bagian 8b butir 2): entri baru Delete `Skip Free {runId}-067` (selisih jumlah total entri terhadap baseline) pada tiap surface (langkah 27, 30, 33) membuktikan surface yang sama mencatat aksi sungguhan yang terjadi pada jendela waktu yang sama dengan aksi No-Op. Asersi absence memakai baseline jumlah total entri (dicatat pada langkah 1 sampai 3 sebelum aksi pemicu pertama), bukan anchor baris seed (S-12).
- Pemeriksaan di surface yang tidak disebut Expected Result suatu TC (mis. Activity Log dan System Log untuk TC-GS-DIV-99, 288, dan 244; Changelog untuk TC-GS-DIV-300) ikut tercakup karena daftar nama diperiksa utuh pada setiap surface dengan baseline yang sama; Expected Result "tidak ada entri log baru" pada TC-GS-DIV-99 dan 288 tidak menyebut surface.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3 (pencatatan baseline jumlah total entri), Search nama Division pada tabel Division sebelum Edit (langkah 4, 8, 12, 15, 18), langkah 7, 11, 14, dan 24 (menunggu aksi selesai, 8b butir 8), langkah 21 (page size 50 supaya kedua baris tampil sekaligus), langkah 25 (memulihkan page size 10; hook `after` tetap cadangan), serta langkah 26, 29, dan 32 (membuka surface log). Search pada langkah 4, 8, 12, 15, dan 18 tidak tertulis di Langkah Uji TC sumber karena tabel A-Z memiliki lebih dari satu halaman.
- Division bernama literal di TC sumber diganti Division milik spec bersuffix, kecuali `Human Resources` (Pre-setup, hanya menjadi target aksi No-Op dan yang dilewati, tidak diubah; pengecualian S-06) dan `Information Technology` (literal, lihat Prerequisites). `Accounting` (TC-GS-DIV-100), `Log Gen 2` (TC-GS-DIV-240), dan `Syslog NoOp` (TC-GS-DIV-300) tidak harus literal karena asersinya tidak bergantung pada nama. `Skip Free {runId}-067` menggantikan `Information Technology` sebagai Division bebas relasi pada TC-GS-DIV-244 supaya baris Population yang dipakai TC-GS-DIV-288 tidak terhapus.
- Spec memuat 34 langkah, dengan sembilan langkah baca-log di akhir; enam TC berbagi satu baseline log dan satu rangkaian pembacaan tiga surface (satu kelas harness, asersi absence); memecahnya per TC melipatgandakan pencatatan baseline dan pembacaan Changelog, Activity Log, dan System Log. Blok Edit No-Op berdiri sendiri, sedangkan pembacaan log di akhir melanjutkan hasil seluruh blok aksi.
- Temuan untuk QA:
  - TC-GS-DIV-99 Expected Result a ("Kandidat `HR` hanya bentrok dengan record itu sendiri sehingga tidak dihitung bentrok") dan TC-GS-DIV-288 Expected Result b bagian pertama adalah penjelasan logika server tanpa elemen UI yang bisa diamati; diasersi di spec 028 lewat hasil Code, bukan terpisah.
  - TC-GS-DIV-99 Precondition c ("Division `Accounting` (Code `ACC`) sudah dibuat") tidak dipakai langkah TC; tidak dimasukkan ke spec.
  - TC-GS-DIV-100 Post Condition ("Accounting tidak berubah dan Last Updated tidak berubah") tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-GS-DIV-240 dan 300 tidak menyebut kondisi hasil Edit pada UI selain toast; spec hanya memverifikasi toast pada langkah 17 dan 20, sedangkan Expected Result log diasersi pada langkah 28, 31, dan 34.
  - TC-GS-DIV-244 Post Condition ("Entri Delete hanya untuk Division yang terhapus") sama dengan Expected Result a dan b sehingga tidak diasersi terpisah.
