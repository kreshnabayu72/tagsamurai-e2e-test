---
id: TC-GS-ROLE-E2E-013-mobile-detail-long-press-multi-select-dan-bulk-remove
title: "Mobile Detail Role: Long Press Multi-Select, Floating Bottom Bulk Bar, dan Select All"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-32
coverage:
  web: automated
  mobile: automated
---

# Mobile Detail Role: Long Press Multi-Select, Floating Bottom Bulk Bar, dan Select All

## Prerequisites

- Mode: FE+BE.
- Perangkat: satu perangkat Android uji (kelompok Android uji A sampai E, perangkat fisik bersama) dengan aplikasi Android native terpasang. Spec menulis `parallel: false` karena perangkat dipakai bersama; suite ini juga serial.
- Akun aktor: Total Control (Ahmad Fauzi) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di aplikasi mobile sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Layar awal spec: Role & Permission > Tab System di aplikasi mobile dibuka di hook `beforeEach`.
- Flag Guided Tooltip: spec mobile tidak memakai hook flag suite (lihat `suite.md`, Hook suite) dan tidak menguji Guided Tooltip.
- Data Pre-setup yang dibaca: Detail "Manage TAG" dengan baris Doni Pratama (Pre-setup #10) dan Siti Nurhaliza (Pre-setup #4, baris role Manage TAG), ditambah baris Ahmad Fauzi (aktor) dan Budi Santoso (Default User) yang checkbox-nya disabled bila ada. Spec tidak membuat, mengubah, atau menghapus data; `[Remove]` tidak dijalankan.
- Kemampuan teknis: long-press dan tap pada perangkat Android.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-32: Detail multi-select lewat long press dan bulk Remove

1. Tap `[⋯]` pada card "Manage TAG", lalu tap Detail
2. Verifikasi toggle Read tampil pada card Doni Pratama
3. Verifikasi toggle Update tampil pada card Doni Pratama
4. Verifikasi toggle Create dan Delete tidak ada pada card Doni Pratama
5. Long-press card Doni Pratama
6. Verifikasi checkbox muncul di kiri tiap card
7. Verifikasi card Doni Pratama tercentang
8. Verifikasi Floating Bottom Bulk Bar tampil dengan `[✕]`
9. Verifikasi Floating Bottom Bulk Bar menampilkan counter "1 Selected"
10. Verifikasi Floating Bottom Bulk Bar menampilkan `[Select All]`
11. Verifikasi Floating Bottom Bulk Bar menampilkan aksi `[Remove]` dengan severity danger
12. Tap card Siti Nurhaliza yang checkbox-nya enabled
13. Verifikasi counter "2 Selected"
14. Tap `[Select All]`
15. Verifikasi semua card pada halaman aktif yang checkbox-nya enabled tercentang
16. Verifikasi counter "[N] Selected" sesuai jumlah card tercentang itu
17. Tap `[✕]` pada Floating Bottom Bulk Bar
18. Tap `[⋯]` pada card Doni Pratama
19. Verifikasi row action Remove tersedia di `[⋯]` card
20. Tutup menu `[⋯]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 17 (`[✕]` mengakhiri selection mode) dan langkah 20 (tutup menu `[⋯]`).
- Langkah 2 sampai 4 menjalankan Expected a (card per user menampilkan toggle Read dan Update saja); langkah 18 sampai 19 menjalankan Expected f setelah selection mode diakhiri, supaya `[⋯]` card dapat diketuk.
- Langkah 11 memeriksa `[Remove]` pada Floating Bottom Bulk Bar hanya tampil; aksi Remove massal tidak dijalankan karena TC-GS-ROLE-32 tidak memuat langkah mengetuknya.
- Temuan untuk QA:
  - TC-GS-ROLE-32 langkah 4 tidak menyebut card mana yang dipilih ("satu card lain yang checkbox-nya enabled"); spec memakai Siti Nurhaliza.
  - Judul TC-GS-ROLE-32 menyebut "bulk Remove" tetapi langkah dan Expected hanya sampai tampilnya `[Remove]` di Floating Bottom Bulk Bar; eksekusi bulk Remove tidak diasersi di spec ini.
  - Guided Tooltip di aplikasi mobile tidak dinyatakan TC; hook flag suite tidak berlaku untuk spec mobile, dan bila walkthrough tampil di perangkat, kemampuan menyetel flag disediakan tim FE/BE.
