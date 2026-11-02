---
id: TC-AC-SG-E2E-074-modal-changelog-setup-column-tutup-modal-dan-snapshot-immutable
title: "Modal Changelog: Setup Column, Tutup Modal, dan Snapshot Immutable"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-267
  - TC-AC-SG-271
  - TC-AC-SG-272
coverage:
  web: automated
---

# Modal Changelog: Setup Column, Tutup Modal, dan Snapshot Immutable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Akun kedua (ganti akun pada TC-AC-SG-272): Total Control entitas `Distributor Race` (Pre-setup #32) `totalControlRaceA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_RACEA_PASSWORD`.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Data milik spec (S-06, S-12), di-seed Fixture BE di hook `before`: group level 1 `Race Lain {runId}-074` pada tree `Distributor Race` (Pre-setup #32), dipakai TC-AC-SG-272 sebagai pengganti `Race Lain`. Nama hasil rename: `Race Lain Dua {runId}-074` lalu `Race Lain Tiga {runId}-074`. Hook `after` menghapus group milik spec itu lewat Fixture BE. Efek pada tree `Distributor Race`: Last Updated, Modified By, dan entri audit trail Changelog baru (Edit, Edit, Delete) tidak dipulihkan karena audit trail permanen; asersi memakai nama bersuffix unik (baseline nol, S-12).
- Preferensi kolom tabel di browser dihapus di hook `before` dan `after` spec ini (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE (lihat `suite.md`). Spec ini menyimpan konfigurasi kolom Modal Changelog (TC-AC-SG-267).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-271: Modal Changelog ditutup lewat ikon close atau Esc, bukan klik backdrop

1. Klik ikon Changelog pada toolbar
2. Klik area gelap di luar modal
3. Verifikasi modal Changelog tetap terbuka (klik backdrop tidak menutup modal)
4. Tekan Esc
5. Verifikasi modal Changelog tertutup

### TC-AC-SG-267: Setup Column Changelog: Overlay dan modal dengan cache terpisah

6. Catat daftar kolom tabel utama Group List sebelum Setup Column
7. Klik ikon Changelog pada toolbar
8. Klik header kolom Actions kosong
9. Verifikasi Overlay Column Visibility terbuka dari kolom Actions kosong sebagai trigger
10. Hide kolom Old Value pada Overlay Column Visibility
11. Buka `Setup Column...`, pin kolom Date, lalu klik `[Save]`
12. Tutup modal Changelog lewat `[✕]`
13. Klik ikon Changelog pada toolbar
14. Verifikasi kolom Old Value tersembunyi setelah modal dibuka kembali
15. Verifikasi kolom Date terpin setelah modal dibuka kembali
16. Tutup modal Changelog lewat `[✕]`
17. Verifikasi kolom tabel utama Group List sama dengan daftar yang dicatat pada langkah 6 (cache terpisah per tabel)

### TC-AC-SG-272: Entri Changelog lama tidak berubah setelah perubahan berikutnya (snapshot immutable)

18. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Race`
19. Buka halaman `Settings > Group` lewat sidebar
20. Rename `Race Lain {runId}-074` menjadi `Race Lain Dua {runId}-074` lewat row action `Edit` dan `[Save]`
21. Rename `Race Lain Dua {runId}-074` menjadi `Race Lain Tiga {runId}-074` lewat row action `Edit` dan `[Save]`
22. Tunggu aksi selesai (modal Edit Group tertutup)
23. Klik ikon Changelog pada toolbar
24. Ketik Search `{runId}-074` pada toolbar modal, tekan Enter
25. Verifikasi entri Edit pertama menampilkan Old Value `Race Lain {runId}-074` dan New Value `Race Lain Dua {runId}-074`
26. Verifikasi entri Edit kedua menampilkan Old Value `Race Lain Dua {runId}-074` dan New Value `Race Lain Tiga {runId}-074`
27. Verifikasi entri pertama tidak berubah setelah rename kedua: Old Value dan New Value tetap sama
28. Verifikasi kolom Group Name kedua entri Edit berisi nama sesudah perubahan (`Race Lain Dua {runId}-074` dan `Race Lain Tiga {runId}-074`)
29. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 6 (baseline kolom tabel utama), penutupan modal Changelog (S-09), langkah 22 (Tunggu aksi selesai sebelum membuka Changelog, bagian 8b butir 8), langkah 24 (Search untuk menemukan entri milik spec, R-16), dan penutupan modal di akhir.
- Urutan TC dalam spec: 271, 267, 272. TC-AC-SG-267 menyimpan konfigurasi kolom Changelog dan TC-AC-SG-272 memakai akun lain sehingga ditaruh paling akhir sesudah Step ganti akun; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3).
- TC-AC-SG-269 (Download Changelog) ada di spec TC-AC-SG-E2E-114.
- Entri seed Changelog tidak diasersi absolut: entri TC-AC-SG-272 dicari lewat nama bersuffix unik (baseline nol), bukan posisi teratas (S-12, S-14). Dua entri Edit dapat bertanggal menit yang sama, jadi urutan relatif keduanya tidak diasersi; yang diasersi adalah isi tiap entri.
- Temuan untuk QA:
  - TC-AC-SG-272 memakai nama literal `Race Lain`, `Race Lain Dua`, `Race Lain Tiga` pada tree `Distributor Race`; spec memakai nama bersuffix `{runId}-074` pada group milik spec (S-06, S-12; Lampiran A tidak memuat pengecualian modul ini).
  - TC-AC-SG-272 "entri pertama tidak berubah" dibaca sebagai: setelah rename kedua, isi entri Edit pertama tetap sama; TC tidak memberi langkah observasi sebelum rename kedua.
  - TC-AC-SG-267 butir b (kolom Actions kosong sebagai trigger) diasersi lewat pembukaan Overlay Column Visibility dari kolom itu.
  - TC-AC-SG-267 menyebut "pin kolom Date" tanpa menyebut cara menutup Setup Column selain `[Save]`; spec memakai `[Save]`.
