---
id: TC-AC-ACC-E2E-127-delete-client-berfoto-dan-nama-dipakai-ulang
title: "Delete Client Menghapus File Photo dan Nama Client yang Sudah Dihapus Dapat Dipakai Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-949
  - TC-AC-ACC-231
coverage:
  web: automated
---

# Delete Client Menghapus File Photo dan Nama Client yang Sudah Dihapus Dapat Dipakai Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun):
  - Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`, lewat Step ganti akun eksplisit di blok kedua. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Dinamis milik spec (bersuffix unik per run, S-12): Company Name `PT Foto Hapus Uji {runId}-127`; PIC Name `Rina Kartika`; PIC Email `rina.kartika+{runId}-127@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name `Sari`, Last Name `Pratiwi`, Email `foto.hapus+{runId}-127@qwertysystem.net`, Division `Finance`; Group `Cabang Menteng`. Hook `after` menghapus Client hasil blok kedua lewat API bila masih ada.
- Berkas uji foto `foto-uji-a.jpg` (JPG 200 KB) tersedia di mesin uji dan dipakai untuk unggah foto.
- Kemampuan teknis: unggah foto dari berkas lokal; membaca atribut `src` thumbnail Photo; membuka URL foto di tab baru atau permintaan GET ke URL itu dan mengamati bahwa berkas gambar tidak dikembalikan (disediakan tim FE).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-949: Delete Client menghapus file Photo-nya: URL foto tidak lagi dapat dibuka

1. Klik `[+ New Client]`
2. Pilih foto `foto-uji-a.jpg`
3. Isi Company Name `PT Foto Hapus Uji {runId}-127`, PIC Name `Rina Kartika`, PIC Email `rina.kartika+{runId}-127@qwertysystem.net`, Address `Jl. Sudirman No. 10`, Country `Indonesia`, State `DKI Jakarta`, City `Jakarta Selatan`, Postal Code `12190`, Default User First Name `Sari`, Last Name `Pratiwi`, Email `foto.hapus+{runId}-127@qwertysystem.net`, dan Division `Finance`
4. Pilih Group "Cabang Menteng" pada tree Select Group
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, client has been created."
7. Ketik Search `PT Foto Hapus Uji {runId}-127`, tekan Enter
8. Klik `[⋯]` pada baris `PT Foto Hapus Uji {runId}-127` → klik `Detail`
9. Verifikasi header Detail menampilkan thumbnail Photo (bukan avatar inisial)
10. Catat atribut `src` thumbnail Photo di header Detail sebagai URL foto
11. Klik breadcrumb "Client"
12. Ketik Search `PT Foto Hapus Uji {runId}-127`, tekan Enter
13. Klik `[⋯]` pada baris `PT Foto Hapus Uji {runId}-127` → klik `Delete`
14. Verifikasi dialog Title "Delete Client" dengan bullet `• PT Foto Hapus Uji {runId}-127`
15. Verifikasi dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
16. Ketik nama persis `PT Foto Hapus Uji {runId}-127` pada input "Type the client name to confirm", centang "I understand this action cannot be undone", klik `[Delete]`
17. Verifikasi toast sukses "Success, client has been deleted."
18. Buka URL foto di tab baru
19. Verifikasi URL foto tidak menampilkan gambar (permintaan ke URL itu tidak mengembalikan berkas gambar)

### Blok Total Control

20. Ganti akun: logout lalu login sebagai Total Control A-01

#### TC-AC-ACC-231: Nama Client yang sudah dihapus dapat dipakai ulang

21. Klik `[+ New Client]`
22. Isi Company Name `PT Foto Hapus Uji {runId}-127` (nama Client yang baru dihapus pada TC-AC-ACC-949), PIC Name `Rina Kartika`, PIC Email `rina.kartika+{runId}-127@qwertysystem.net`, Address `Jl. Sudirman No. 10`, Country `Indonesia`, State `DKI Jakarta`, City `Jakarta Selatan`, Postal Code `12190`, Default User First Name `Sari`, Last Name `Pratiwi`, Email `foto.hapus+{runId}-127@qwertysystem.net`, dan Division `Finance`
23. Pilih Group "Cabang Menteng" pada tree Select Group
24. Klik `[Submit]`
25. Verifikasi toast sukses "Success, client has been created."

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC-AC-ACC-231 sesudah TC-AC-ACC-949 mengikuti syarat TC-AC-ACC-231 ("nama Client yang baru dihapus"): langkah 21 sampai 25 memakai nama yang dihapus pada langkah 16; langkah dependensi Create disalin dari TC-AC-ACC-949 (S-04). Ganti akun (langkah 20) sah karena TC-AC-ACC-231 menyebut Total Control dan tetap bermakna sebagai bagian sendiri.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 11 (kembali ke List); Search yang menemukan baris target (langkah 7 dan 12). Pembersihan Client hasil TC-AC-ACC-231 dilakukan di hook `after` (TC-AC-ACC-231 tidak punya Post Condition).
- Post Condition TC-AC-ACC-949 ("dibuat dan dihapus oleh TC") sudah menjadi langkah; TC-AC-ACC-231: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-231 langkah 1 ("Buat Client dengan nama Client yang baru dihapus") tidak menyebut data Create lain dan tidak menyebut Client mana yang baru dihapus; spec memakai nama dan data dari TC-AC-ACC-949. Precondition TC-AC-ACC-231 juga tidak menyebut Client yang dihapus.
  - TC-AC-ACC-231 tidak punya Post Condition untuk Client hasil Create; pembersihan di hook `after`.
