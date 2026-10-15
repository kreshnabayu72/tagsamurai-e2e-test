---
name: tagsamurai-e2e-audit
description: Audit hasil generate e2e TAG Samurai untuk satu suite: traceability TC granular → spec.md → web.test.ts, kepatuhan konvensi efisiensi dan data. Hanya melaporkan temuan, tidak memperbaiki.
---

# Audit E2E (report-only)

Skill ini hanya **melaporkan**. Jangan mengubah file apa pun, termasuk spec, script, dan TC granular. Tampilkan temuan ke user dan tunggu instruksi. Jangan langsung memperbaiki walau temuannya jelas.

Rujukan aturan: `docs/e2e-conventions.md`. Skill ini melengkapi `spectra lint`, yang hanya memeriksa format. Jalankan `python scripts/check-suite.py specs/<Suite> <path tc-[modul].md> docs/coverage/<Suite>.md` lebih dulu (cakupan, duplikat sourceTc, id folder, Mode, spec di atas 35 langkah tanpa alasan, jumlah TC di coverage, asersi absence tanpa anchor) dan jalankan `python scripts/sync-skills.py --check`; lalu Jalankan `spectra lint --strict specs/<Suite>` dan `pnpm type-check` dulu, lalu periksa hal-hal yang tidak dicakup linter.

## Aturan umum

- **Satu sumber aturan.** Kategori B, D, dan E memakai `docs/e2e-conventions.md` bagian 10 (S-01 sampai S-15) beserta bagian konvensi lain. Setiap temuan B/D/E menyebut id aturannya (contoh `S-04`). Jangan menandai hal yang tidak ada di daftar itu atau di konvensi; kalau menemukan pola yang menurut Anda perlu aturan baru, taruh di "Perlu keputusan" sebagai usulan aturan, bukan sebagai temuan.
- **Baca dulu catatan generate.** Sebelum menilai, baca `## Notes` tiap spec (butir "Temuan untuk QA", langkah penghubung, penyimpangan urutan) dan, bila ada, laporan akhir generate / `progress-e2e-generate-spec.md`. Hal yang sudah tercatat di sana dan sah menurut konvensi bukan temuan; masalah TC yang sudah tercatat dipisah ke bagian "Temuan sumber yang sudah diketahui" (lihat format laporan).
- **Tingkat temuan.**
  - **Berat:** cakupan hilang atau salah (TC tanpa spec, butir Expected tanpa `Verifikasi`, asersi berlawanan dengan TC, `sourceTc` salah).
  - **Sedang:** spec tidak bisa dieksekusi apa adanya atau hasilnya bisa lulus/gagal bukan karena perilaku yang diuji (langkah bersyarat, state bocor antar-TC, data tidak dijamin, kebutuhan tidak ada di Prerequisites, menumpang spec lain).
  - **Ringan:** kosmetik atau dokumentasi (langkah penghubung tidak dicatat di Notes, Prerequisites memuat data tak dipakai, urutan atau penghematan langkah).
- **Dua daftar, bukan satu.** Penyebab (1) kesalahan hasil generate masuk daftar temuan spec. Penyebab (2) kekurangan TC sumber atau konvensi masuk daftar "Temuan sumber" untuk pemilik TC/konvensi dan tidak menentukan status audit spec.

## Input

Path suite (contoh `specs/GlobalSettings/User`) dan path `tc-[modul].md` sumbernya.

## Pemeriksaan

**A. Traceability (arah TC granular → spec)**
- Ekstrak semua id TC di `tc-[modul].md`. Untuk tiap id: apakah muncul di `sourceTc` spec mana pun, atau tercatat di `docs/coverage/<Suite>.md` sebagai TC hanya-BE (dengan id TC BE bila ada)?
- Satu-satunya alasan sah sebuah TC tidak punya spec adalah hanya-BE. Alasan lain, termasuk "sudah dicakup FE", "tidak layak", "butuh waktu/kuota/race/mock", atau label "Manual", adalah temuan.
- Spec hanya-FE harus punya baris `Mode: mock` di `## Prerequisites` beserta kebutuhan mock-nya (endpoint dan respons yang dipaksa).
- Cek Changelog `tc-[modul].md` sebelum menyimpulkan ada id yang hilang (id yang sudah dihapus resmi bukan temuan).

**B. Traceability (arah spec → TC granular)**
- Setiap `sourceTc` menunjuk id yang benar-benar ada di `tc-[modul].md`.
- Isi spec sesuai TC sumbernya (role, precondition, langkah, expected result). Bandingkan per TC yang digabung. Langkah atau expected result yang hilang, ditambah, atau berubah makna adalah temuan.
- `priority` sesuai mapping bagian 8 konvensi (tertinggi dari TC sumber).
- `caseType` mengikuti aturan spec gabungan bagian 8 konvensi (jenis alur utama yang dominan). Jangan menandai temuan hanya karena TC sumber campuran jenisnya.
- Label tombol dan cara menutup form sesuai bagian 9 konvensi (Create `[Submit]`, Edit `[Save]`, `[Clear Field]`, `✕`/`Esc`, tanpa `[Cancel]` pada modal). Cocokkan ke `prd-conventions.md` §24.1, bukan hanya ke TC.
- `coverage.web` tidak dinilai terhadap `status`. Kolom itu hanya jenis pengujian, progres dibaca dari `status`.
- Bahasa spec Indonesia (bagian 7 konvensi): narasi Indonesia, teks UI persis seperti di aplikasi, langkah asersi diawali `Verifikasi`. Spec berbahasa Inggris adalah temuan.
- Aturan asersi bagian 8b konvensi: request langsung ke server tidak mengasersi perilaku FE; asersi absence punya anchor positif yang terhubung ke pemicu; batas waktu dihitung dari waktu terbit artefak; rate limit menyebut endpoint dan payload flood; state sementara diasersi sebelum langkah yang mengubahnya. Pelanggaran yang bersumber dari expected TC dilaporkan sebagai jenis (2), diarahkan ke perbaikan TC.
- Spec Role Matrix (bagian 3a): dipisah positif dan negatif, ada tabel "Role yang diuji", dan tiap kombinasi role × aksi punya TC granular sumber. Kombinasi tanpa TC sumber adalah temuan.

**C. Spec → script**
- Tiap langkah `Verifikasi ...` di spec.md punya assertion di `web.test.ts`, dan urutannya sama.
- Script tidak berisi aksi atau assertion yang tidak ada di spec.md.
- `it()` title = `title`. `@step` = `Step.*` (linter sudah memeriksa, konfirmasi hasilnya).
- Assertion tidak dangkal: bukan hanya cek elemen ada padahal expected result menyebut isi, badge, atau toast tertentu.

**D. Efisiensi dan independensi**
- Spec tidak bergantung pada data atau hasil spec lain (cari nama data yang dibuat di spec lain).
- Login dan seed dilakukan di hook, bukan diulang di tiap `it()`.
- Jumlah buka form/modal per spec tidak lebih dari jumlah kejadian yang menutup form. Tandai spec yang membuka form ulang tanpa alasan.
- Screening ada di awal spec. Validasi yang diblokir ada sebelum aksi sukses. Kasus menutup form ada di akhir.
- Tidak ada dua spec dengan alur dan assert yang sama, dan tidak ada spec yang seharusnya digabung (topik sama, bisa satu alur) tetapi terpisah. Sebaliknya, topik aksi berbeda dengan kondisi data bervariasi (Delete, Toggle Active, Remove Access) yang tergabung dalam satu spec adalah temuan.
- Aksi yang menghapus data ada di akhir spec. Spec yang memakai Select All lalu Bulk Delete tidak berjalan paralel dan tidak mendahului spec lain.
- Spec tidak mencampur role atau entity berbeda tanpa Step ganti akun, kecuali spec Role Matrix.
- Setup yang dibutuhkan satu spec tidak ditaruh di `global-hooks`.
- Spec yang membuat data punya cleanup, dan spec tanpa pembuatan data tidak menumpang data spec lain.

**E. Data**
- Tidak ada password, token, atau kredensial di spec, fixture, atau script.
- Data yang harus unik memakai suffix dinamis. Data yang dibuat spec dibersihkan di hook.
- Setiap data, akun, kondisi environment, dan kemampuan teknis yang dipakai langkah spec tercantum di `## Prerequisites`, bukan hanya di `## Notes`.
- Data pre-setup mengacu ke fixture yang cocok dengan tabel Data Uji Pre-setup di TC sumber.

**F. Kode**
- Tidak ada selector mentah di `web.test.ts`. Tidak ada xpath atau nth-child di Page Object.
- Tidak ada `sleep` atau jeda tetap, komentar di kode, import manual, atau `describe`/`test`.
- Struktur: suite di `specs/<ModulBesar>/<SubModul>/`, nama folder TC = id, penamaan entitas berprefix modul, tidak ada file di luar folder standar.

**G. Sapuan pola (wajib sebelum laporan final)**
- Setiap temuan yang bersumber dari satu TC atau satu spec dijadikan pola (frasa, struktur, atau jenis kesalahan), lalu dicari di seluruh `tc-[modul].md` dan seluruh spec suite dengan grep. Contoh: expected perilaku FE pada TC yang langkahnya request langsung ke server ditemukan di TC-132, maka cari juga di TC lain yang memakai frasa "langsung ke server" atau "fixture BE".
- Tiap kemunculan pola dilaporkan sebagai baris temuan sendiri (atau digabung dalam satu baris dengan daftar lengkap ID-nya), bukan hanya instance yang pertama ketemu. Kolom `Bukti` memuat perintah grep dan jumlah kemunculannya.
- Perbaikan yang diusulkan wajib mencakup semua kemunculan pola; temuan yang hanya menyebut satu instance padahal polanya muncul lebih dari satu dianggap belum selesai.
- Putaran audit ulang (setelah perbaikan) mengulang sapuan ini untuk pola yang sudah ditemukan dan menjalankan lagi `scripts/check-suite.py`; audit tidak dinyatakan selesai sebelum kedua hal itu bersih atau dicatat sebagai keputusan.
- Hasil sapuan yang tidak menemukan kemunculan lain ditulis eksplisit ("pola X: 1 kemunculan, sudah disapu") supaya jelas bahwa sapuan dilakukan.

## Format laporan

1. Ringkasan: jumlah TC granular, jumlah spec, TC diotomasi / dilewati / belum tercakup, hasil lint dan type-check.
2. Tabel temuan spec (penyebab 1), diurutkan dari yang paling berat: `No` | `Kategori (A-F)` | `Id aturan` | `Tingkat` | `Spec/TC` | `Temuan` | `Bukti (file:baris)` | `Rekomendasi` | `Diubah di`. Temuan Ringan boleh dikelompokkan per tema dalam satu baris; Berat dan Sedang satu baris per temuan.
   - `Rekomendasi`: perubahan konkret yang menutup temuan (apa yang ditulis, dipindah, atau dihapus), bukan sekadar "perbaiki".
   - `Diubah di`: file yang harus diedit, salah satu atau lebih dari `spec` (spec.md suite), `TC` (`tc-[modul].md`), `PRD` (PRD modul), `konvensi` (`docs/e2e-conventions.md`), `skill generator` (`tagsamurai-e2e-generate-spec`), `coverage` (`docs/coverage/<Suite>.md`). Temuan penyebab (2) tidak boleh hanya `spec`. Temuan penyebab (1) yang berulang di beberapa spec juga mencantumkan `skill generator` supaya tidak terulang.
3. Tabel "Temuan sumber" (penyebab 2: TC, PRD, atau konvensi): `No` | `Pemilik` | `Spec/TC terdampak` | `Temuan` | `Rekomendasi` | `Sudah dicatat di Notes/laporan generate (ya/tidak)`. Temuan yang sudah dicatat tampil di sini sekali saja, tidak diulang di tabel 2.
4. Bagian "Perlu keputusan" untuk hal yang tidak bisa disimpulkan dari file (contoh: TC sumber ambigu, atau selector belum ada di app). Tiap butir memuat opsi beserta rekomendasi pilihan dan alasannya.
5. Bagian "Rekomendasi urutan perbaikan": kelompokkan temuan per file tujuan (`TC`/`PRD`/`konvensi` dulu karena sumber, lalu `skill generator`, lalu `spec`/`coverage`), dan sebut workflow yang dipakai (contoh `audit-testcase` untuk TC, `e2e-generate-spec` untuk spec).

Bedakan dua jenis penyebab pada tiap temuan: (1) kesalahan hasil generate, atau (2) kekurangan di TC sumber atau konvensi. Untuk jenis (2) arahkan ke perbaikan sumber, jangan ke spec.

## Status audit

Audit spec dinyatakan bersih bila tidak ada temuan Berat atau Sedang pada tabel 2; Ringan hanya dilaporkan sebagai jumlah dan tidak memblokir. Tabel "Temuan sumber" dilaporkan ke pemilik TC/konvensi dan tidak memblokir status spec.
